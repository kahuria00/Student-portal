
from django.test import TestCase
from.models import Teacher
import datetime
from.forms import TeacherForm
class CreateTeacherTestCase(TestCase):
    def setUp(self):
        self.data={
        "first_name":"charity",
        "last_name":"Wanjiru",
        "registration_number":"6677865",
        'place_of_residence':"Kilimani",
        "phone_number":"070010533323",
        'email':"charie@gmail.com",
        'Id_Number':"987768787",
        "dateJoined":datetime.date.today(),
        "profession":"Developer"
    
        }
        self.bad_data={
        "first_name":"charity",
        "last_name":"Wanjiru",
        "registration_number":"6677865",
        "place_of_residence":"Kilimani",
        "phone_number":"076533323",
        "email":"charrie@gmail.com",
        "Id_Number":"987768787",
        "DateJoined":"datetime.date.today()",
        "profession":"Developer"
        }
    
    def test_teacher_form_always_valid_data(self):
        form=TeacherForm(self.data)
        self.assertTrue(form.is_valid())
        
    def test_bad_teacher_form_reject_invalid_data(self):
        form=TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())
# Create your tests here.