from django.shortcuts import render
from django.shortcuts import render
from .serializers import CourseExamInfoSerializer
from .helpers import parse_school_exam_timetable, nursing_exam_timetable_parser
from notifications.serializers import MessageSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


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
        