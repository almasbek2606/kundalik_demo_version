# Generated by Django 4.2.2 on 2023-07-15 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('statistic', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachermodel',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statistic.subjectmodel'),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='parents',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.parentsmodel'),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.schoolmodel'),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='var_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.classmodel'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
