from django.contrib import admin
from .models import SchoolModel, ClassModel
# Register your models here.

admin.site.register(SchoolModel)
admin.site.register(ClassModel)