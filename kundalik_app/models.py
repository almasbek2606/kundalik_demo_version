from django.db import models
from datetime import datetime


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=65)
    fullname = models.CharField(max_length=65)
    date_of_birth = models.DateField(default=datetime.now)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class School(models.Model):
    number = models.IntegerField(default=1)
    address = models.CharField(max_length=70)

    def __str__(self):
        return self.address


class Subject(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Students(models.Model):
    active = models.BooleanField(default=False)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Teacher(Person):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    salary = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now)
    mark = models.IntegerField(max_length=5)


class Attendance(models.Model):
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now)
