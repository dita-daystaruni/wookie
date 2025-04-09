from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .helpers import parse_school_exam_timetable, nursing_exam_timetable_parser
from .models import CoursesExamInfo
from .serializers import CourseExamInfoSerializer, MessageSerializer


class ParseTimeTablesAPI(APIView):
    """
    Will Handle Parsing Of Exam Timetable
    """
    def post(self, request, *args, **kwargs):
        """
        Handles Parsing of TimeTables
        """
        file = request.data.get("file")
        file_to_parse = request.data.get("file_name")
        if file_to_parse == "school_exams":
            courses = parse_school_exam_timetable(file)
            # TODO consider using serializer many=True
            with transaction.atomic():
                for course in courses:
                    serializer = CourseExamInfoSerializer(data=course)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        # duplicate course, we handle by deleting duplicate courses
                        if serializer.errors.get('course_code')[0] == \
                            "courses exam info with this course code already exists.":
                            # TODO log this in future
                            print(course)
                            dup_course = CoursesExamInfo.objects.get(
                                course_code=course["course_code"],
                            )
                            dup_course.delete()
                            continue
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif file_to_parse == "nursing_exams":
            courses = nursing_exam_timetable_parser(file)
            for course in courses:
                serializer = CourseExamInfoSerializer(data=course)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            message = {"message": "file to parse options are school_exams or nursing_exams"}
            serializer = MessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
         # parsing and writing to database was successful
        message = {"message": "Successfully Parsed and Saved To Database"}
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        """
        Updates the Course Info
        """
        file = request.data.get("file")
        file_to_parse = request.data.get("file_name")

        if file_to_parse == "school_exams":
            courses = parse_school_exam_timetable(file)
            for course in courses:
                print(course)
                exam_course = CoursesExamInfo.objects.get(course_code=course["course_code"])
                serializer = CourseExamInfoSerializer(exam_course, data=course)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif file_to_parse == "nursing_exams":
            courses = nursing_exam_timetable_parser(file)
            for course in courses:
                exam_course = CoursesExamInfo.objects.get(course_code=course["course_code"])
                serializer = CourseExamInfoSerializer(exam_course, data=course)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
         # parsing and writing to database was successful
        message = {"message": "Successfully Parsed and Saved To Database"}
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ExamsCourseInfoAPI(APIView):
    """"
    Will be Used to return exams info 
    about a course
    """
    def post(self, request, *args, **kwargs):
        """
        Receives a list of course codes and
        Returns a list of exam course info
        """
        course_codes = request.data.get("course_codes")
        exams_info = [] # will hold the Data to return 
        for course_code in course_codes:
            # adding optional spaces to the search query to match spaces between searches
            course_code = course_code.replace(" ", "")
            if "NUR" in course_code or "NUP" in course_code:
                course_code = course_code[:-1]
            mod_course_code = "".join(f"{char}\s*" for char in course_code)
            for exam_info in CoursesExamInfo.objects.filter(
                course_code__iregex = f".*{mod_course_code}.*").all():
                exams_info.append(exam_info)

        serializer = CourseExamInfoSerializer(exams_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ExamInfoTruncateAPI(APIView):
    """
    Used to truncate courses for a particular School
    """
    def delete(self, request, *args, **kwargs):
        """
        Deletes All course for a school
        """
        school = request.data.get("school")
        if not school:
            message = {"message": "School Is Required"}
            serializer = MessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        if school == "nursing":
            courses_trunc = []
            course_codes = ["NUR", "NUP"]
            for course_code in course_codes:
                course_code = course_code[:-1]
                mod_course_code = "".join(f"{char}\s*" for char in course_code)
                for exam_info in CoursesExamInfo.objects.filter(
                    course_code__iregex = f".*{mod_course_code}.*").all():
                    courses_trunc.append(exam_info)
            for course_trunc in courses_trunc:
                course_trunc.delete()
            message = {"message": "Successfully Truncated Nursing TimeTable"}
            serializer = MessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif school == "daystar":
            courses_trunc = []
            course_codes = ["NUR", "NUP"]
            for course_code in course_codes:
                course_code = course_code[:-1]
                mod_course_code = "".join(f"{char}\s*" for char in course_code)
                for exam_info in CoursesExamInfo.objects.exclude(
                    course_code__iregex = f".*{mod_course_code}.*").all():
                    courses_trunc.append(exam_info)
            for course_trunc in courses_trunc:
                course_trunc.delete()
            message = {"message": "Successfully Truncated The School TimeTable"}
            serializer = MessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            message = {"message": "Wrong Type Of School"}
            serializer = MessageSerializer(message)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
