from .views import *
from django.urls import path

urlpatterns = [
    path('teacher/', TeacherView.as_view()),
    path('teacher/<pk>/', TeacherDetailView.as_view()),
    path('student/', StudentView.as_view()),
    path('student/<pk>/', StudentDetailView)
]
