# Generated by Django 2.2.1 on 2019-11-07 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20190612_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseName',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseNumber',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='teacher.Teacher'),
        ),
    ]