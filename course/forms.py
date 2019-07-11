from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    # courseName=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter course name'}),required=True,max_length=30)
    # # duration_in_month=forms.SmallIntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter duration in months'}))
    # courseNumber=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter course number'}),required=True,max_length=10)
    # course_description=forms.TextField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter course description'}),required=True,max_length=1000)
    
    class Meta:
        model=Course
        fields="__all__"