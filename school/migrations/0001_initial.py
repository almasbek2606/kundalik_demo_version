# Generated by Django 4.2.2 on 2023-07-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=5)),
            ],
            options={
                'db_table': 'class_model',
            },
        ),
        migrations.CreateModel(
            name='SchoolModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(default=1)),
                ('address', models.TextField(default='', max_length=150)),
                ('info', models.JSONField()),
            ],
            options={
                'db_table': 'school',
            },
        ),
    ]
