from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your first name'}),required=True,max_length=50)
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your last name'}),required=True,max_length=50)
	date_of_birth=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your date of birth'}),required=True)
	registration_number=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your registration number'}),required=True,max_length=50)
	place_of_residence=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your place of residence'}),required=True,max_length=50)
	phone_number=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your phone number'}),required=True,max_length=15)
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your email'}),required=True,max_length=25)
	guardian_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your guardian name'}),required=True,max_length=50)
	ID_Number=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter your ID Number'}),required=True)
	DateJoined=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'dd/mm/yy'}),required=True)
	
	class Meta:
		model=Student
		fields="__all__"

