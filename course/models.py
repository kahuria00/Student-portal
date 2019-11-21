from django.db import models
from teacher.models import Teacher

class Course(models.Model):
    courseName=models.CharField(max_length=30,unique=True)
    duration_in_month=models.SmallIntegerField()
    courseNumber=models.CharField(max_length=10,unique=True)
    course_description=models.TextField(max_length=1000)
    teacher=models.ForeignKey(Teacher,on_delete=models.PROTECT,blank=False,null=True)
   
    
    def __str__(self):
        return self.courseName


