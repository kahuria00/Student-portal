from django.db import models
from course.models import Course
import datetime


class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    registration_number=models.CharField(max_length=50)
    place_of_residence=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
    guardian_name=models.CharField(max_length=50)
    ID_Number=models.IntegerField()
    DateJoined=models.DateField()
    courses=models.ManyToManyField(Course)
    image=models.ImageField(upload_to="student_profile",blank=True)

    def full_name(self):
        return self.first_name,self.last_name


    # def calculate_age(born):
    #     today=date.today()
    #     return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    
    def get_age(self):
        today=datetime.date.today()
        return today.year - self.date_of_birth.year
    age=property(get_age)

    def clean(self):
        age=self.age
        if age<18 or age>30:
            raise ValidationError("wrong age bracket 18-30 strictly")
        return age


