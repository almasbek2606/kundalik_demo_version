from rest_framework import serializers
from .models import AttendanceModel, SubjectModel, GradeModel


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceModel
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectModel
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeModel
        fields = '__all__'

