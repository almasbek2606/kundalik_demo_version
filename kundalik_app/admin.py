from django.contrib import admin
from .models import (Subject, School, Students,
                     Person, Teacher, Attendance, Grade)
# Register your models here.

admin.site.register(Subject)
admin.site.register(School)
admin.site.register(Students)
admin.site.register(Person)
admin.site.register(Teacher)
admin.site.register(Attendance)
admin.site.register(Grade)
