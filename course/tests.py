
from django.test import TestCase
from .models import Course
from .forms import CourseForm
from django.urls import reverse
from django.test import Client


client=Client()

class CreateCourseTestCase(TestCase):
   def setUp(self):
       self.data = {
           "courseName":"python",
           "duration_in_month":"4",
           "courseNumber":"667765",
           "course_description":"data",
           
       }
      
       self.bad_data = {
           "courseName":3223 ,
           "duration_in_month":"4",
           "courseNumber":"656677",
           'course_description':"data",
           
       }
    
   def test_course_form_always_valid_data(self):
       form = CourseForm(self.data)
       self.assertTrue(form.is_valid())

   def test_bad_course_form_reject_invalid_data(self):
       form = CourseForm(self.bad_data)
       self.assertFalse(form.is_valid())

   def test_add_course_test(self):
        url=reverse("add_course")
        request=client.post(url,self.data)
        self.assertEqual(request.status_code,200)

   def test_add_course_test_baddata(self):
        url=reverse("add_course")
        request=client.post(url,self.bad_data)
        self.assertEqual(request.status_code,400)