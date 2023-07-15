from django.urls import path
from .views import (AttendanceView, AttendanceDetailView, GradeView,
                    GradeDetailView, SubjectView, SubjectDetailView)

urlpatterns = [
    path('attendance/', AttendanceView.as_view()),
    path('attendance/<pk>/', AttendanceDetailView.as_view()),
    path('grade/', GradeView.as_view()),
    path('grade/<pk>/', GradeDetailView.as_view()),
    path('subject/', SubjectView.as_view()),
    path('subject/<pk>/', SubjectDetailView.as_view())
]
