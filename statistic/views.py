from django.shortcuts import render
from rest_framework import generics
from .models import AttendanceModel, GradeModel, SubjectModel
# Create your views here.
from .serializers import AttendanceSerializer, GradeSerializer, SubjectSerializer


class AttendanceView(generics.ListCreateAPIView):
    queryset = AttendanceModel.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AttendanceModel.objects.all()
    serializer_class = AttendanceSerializer


class GradeView(generics.ListCreateAPIView):
    queryset = GradeModel.objects.all()
    serializer_class = GradeSerializer


class GradeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GradeModel.objects.all()
    serializer_class = GradeSerializer


class SubjectView(generics.ListCreateAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializer


