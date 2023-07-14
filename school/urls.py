from django.urls import path
from .views import SchoolView, SchoolDetailView

urlpatterns = [
    path('school/', SchoolView.as_view()),
    path('school/<pk>/', SchoolDetailView.as_view())
]
