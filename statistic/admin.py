from django.contrib import admin
from .models import SubjectModel, GradeModel, AttendanceModel
# Register your models here.

admin.site.register(SubjectModel)
admin.site.register(GradeModel)
admin.site.register(AttendanceModel)