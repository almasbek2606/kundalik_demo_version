from django.db import models
from datetime import datetime

from django.db.models import CharField


# Create your models here.
class PersonModel(models.Model):
    name = models.CharField(max_length=100, default='')
    fullname = models.CharField(max_length=100, default='')
    date_of_birth = models.DateField(default=datetime.now)
    address = models.TextField()

    def __str__(self) -> CharField:
        return self.name

    class Meta:
        abstract = True


class ParentsModel(PersonModel):
    username = models.CharField(max_length=70, default='')
    password = models.CharField(max_length=70, default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parents'


class StudentModel(PersonModel):
    # from school.models import SchoolModel,ClassModel
    school = models.ForeignKey('school.SchoolModel', on_delete=models.CASCADE)
    var_class = models.ForeignKey('school.ClassModel', on_delete=models.SET_NULL, null=True)
    parents = models.ForeignKey(ParentsModel, default='', on_delete=models.SET_NULL, null=True)
    username = models.CharField(max_length=70, default='')
    password = models.CharField(max_length=70, default='')
    active = models.BooleanField(default=False)
    phone = models.CharField(max_length=13, default='')

    def __str__(self):
        return f"{self.name} {self.fullname}"

    class Meta:
        db_table = 'student'


class TeacherModel(PersonModel):
    # from school.models import SchoolModel
    # from statistic.models import SubjectModel
    subject = models.ForeignKey('statistic.SubjectModel', on_delete=models.CASCADE)
    DEGREE = (
        ("BD", "Bachelor's degree"),
        ("CD", "College degree"),
    )
    degree = models.CharField(max_length=2, choices=DEGREE, default='')
    salary = models.PositiveIntegerField(default=1)
    school = models.ManyToManyField('school.SchoolModel')

    def __str__(self):
        return f"{self.name} {self.fullname}"

    class Meta:
        db_table = 'teacher'
