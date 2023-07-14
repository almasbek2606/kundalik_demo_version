from .models import SchoolModel
from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolModel
        fields = '__all__'
