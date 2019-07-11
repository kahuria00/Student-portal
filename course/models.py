from django.db import models
from teacher.models import Teacher

class Course(models.Model):
    courseName=models.CharField(max_length=30)
    duration_in_month=models.SmallIntegerField()
    courseNumber=models.CharField(max_length=10)
    course_description=models.TextField(max_length=1000)
    teacher=models.ForeignKey(Teacher,on_delete=models.PROTECT)
   
    
    def __str__(self):
        return self.courseName


