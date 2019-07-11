from django.db import models

class Teacher(models.Model):

	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	registration_number=models.CharField(max_length=50)
	place_of_residence=models.CharField(max_length=50)
	phone_number=models.CharField(max_length=15)
	email=models.EmailField(max_length=25)
	ID_Number=models.IntegerField()
	DateJoined=models.DateField()
	profession=models.CharField(max_length=50)
	image=models.ImageField(upload_to="teacher_profile",blank=True)


	def __str__(self):
		return self.first_name+"  "+self.last_name

