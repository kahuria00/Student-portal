from django.db import models
from course.models import Course


class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    registration_number=models.CharField(max_length=50)
    place_of_residence=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField()
    guardian_name=models.CharField(max_length=50)
    ID_Number=models.IntegerField()
    DateJoined=models.DateField()
    courses=models.ManyToManyField(Course)
    image=models.ImageField(upload_to="student_profile",blank=True)

    def __str__(self):
        return self.first_name+"  "+self.last_name


