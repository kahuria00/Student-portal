# Generated by Django 2.2.1 on 2019-06-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='student_profile'),
        ),
        migrations.AlterField(
            model_name='student',
            name='ID_Number',
            field=models.IntegerField(),
        ),
    ]