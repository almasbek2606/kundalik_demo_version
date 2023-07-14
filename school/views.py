from django.shortcuts import render
from .serializers import SchoolSerializer
from .models import SchoolModel
from rest_framework import generics

# Create your views here.


class SchoolView(generics.ListCreateAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer


class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer

