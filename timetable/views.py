from django.shortcuts import render
from django.shortcuts import render
from .serializers import CourseExamInfoSerializer
from .helpers import parse_school_exam_timetable, nursing_exam_timetable_parser
from notifications.serializers import MessageSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CoursesExamInfo

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
            for course in courses:
                serializer = CourseExamInfoSerializer(data=course)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif file_to_parse == "nursing_exams":
            courses = nursing_exam_timetable_parser(file)
            for course in courses:
                serializer = CourseExamInfoSerializer(data=course)
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
            for exam_info in CoursesExamInfo.objects.filter(
                course_code__icontains = course_code).all():
                exams_info.append(exam_info)

        serializer = CourseExamInfoSerializer(exams_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)