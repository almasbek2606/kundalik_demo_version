from django.contrib import admin
from .models import TeacherModel, StudentModel, PersonModel, ParentsModel

# Register your models here.

admin.site.register(TeacherModel)
admin.site.register(StudentModel)
admin.site.register(ParentsModel)
# admin.site.register(PersonModel)
