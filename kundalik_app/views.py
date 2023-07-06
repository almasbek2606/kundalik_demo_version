from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Students
from .serializer import *


# Create your views here.
class ListStudentApiView(APIView):
    def get(self, request, *args, **kwargs):
        all_student = Students.objects.all()
        serializer = StudentSerializer(all_student, many=True)
        return Response(serializer.data)


class DetailStudentApiView(APIView):
    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Students, pk=kwargs['student_id'])
        serializer = StudentSerializer(student)
        return Response(serializer.data)
