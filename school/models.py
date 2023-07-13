from django.db import models


# Create your models here.
class SchoolModel(models.Model):
    number = models.PositiveSmallIntegerField(default=1)
    address = models.TextField(max_length=150, default='')
    info = models.JSONField()

    def __str__(self):
        return str(self.number)

    class Meta:
        db_table = 'school'


class ClassModel(models.Model):
    name = models.CharField(max_length=5, default='')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'class_model'
