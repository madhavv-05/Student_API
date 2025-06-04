from django.shortcuts import render


from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from .response import custom_response




class StudentListCreateAPIView(APIView):
    def get(self,request):
        students=Student.objects.filter(is_deleted=False)
        serializer=StudentSerializer(students,many=True)
        return custom_response(
            status_code=200,
            message="Student List fetched successfully!",
            data=serializer.data
        )
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return custom_response(
                status_code=201,
                message="Student added successfully!",
                data=serializer.data
            )
        return custom_response(
            status_code=400,
            message="validation error",
            data=serializer.errors
        )
    

class StudentUpdateAPIView(APIView):
    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return custom_response(
                status_code=404,
                message="Student not found",
                data=[]
            )

        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return custom_response(
                status_code=200,
                message="Student updated successfully",
                data=[serializer.data]
            )
        return custom_response(
            status_code=400,
            message="Validation failed",
            data=serializer.errors
        )
    
class StudentDeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return custom_response(
                status_code=204,
                message="Student deleted permanently",
                data=[{"id": student.id}]
            )
        except Student.DoesNotExist:
            return custom_response(
                status_code=404,
                message="Student not found",
                data=[]
            )

class StudentSoftDeleteAPIView(APIView):
    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.is_deleted = True
            student.save()
            return custom_response(
                status_code=200,
                message="Student soft-deleted successfully",
                data=[{"id": student.id}]
            )
        except Student.DoesNotExist:
            return custom_response(
                status_code=404,
                message="Student not found",
                data=[]
            )
