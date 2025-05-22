from django.shortcuts import render


from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.filter(is_deleted=False)
    serializer_class = StudentSerializer


class StudentUpdateAPIView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


class StudentDeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


class StudentSoftDeleteAPIView(APIView):
    def put(self, request, id):
        try:
            student = Student.objects.get(id=id)
            student.is_deleted = True
            student.save()
            return Response({"message": "Student soft-deleted successfully"})
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # aws 
        # aws account
        # ec2 server
        # host django application over aws 
        #medium article
