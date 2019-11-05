from django.test import TestCase
from .models import Student
import datetime
from.forms import StudentForm
from django.urls import reverse
from django.test import Client

# Create your tests here.
client=Client()

class StudentTestCase(TestCase):
    def setUp(self):
        self.student=Student(
                first_name="Charity",
                last_name="Wanjiru",
                date_of_birth=datetime.date(1996,2,28),
                registration_number="xyz",
                place_of_residence="Kenya",
                email="charity@yahoo.com",
                phone_number="00007092354",
                guardian_name="namely guardian",
                ID_Number="234333",
                DateJoined=datetime.date(2019,2,1),


            )

    def take_full_name_contain_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())

    def take_full_name_contain_first_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())

    def test_age_is_always_above_17(self):
        self.assertFalse(self.student.clean() < 17)

    def test_age_is_always_below_30(self):
        self.assertFalse(self.student.clean() >30)


class CreateStudentTestCase(TestCase):
    def setUp(self):
        self.data={
                "first_name":"Charity",
                "last_name":"Wanjiru",
                "date_of_birth":datetime.date(1996,2,28),
                "registration_number":"xyz",
                "place_of_residence":"Kenya",
                "email":"charity@yahoo.com",
                "phone_number":"00007092354",
                "guardian_name":"Jane Muthami",
                "ID_Number":"234333",
                "DateJoined":datetime.date(2019,2,1),

    }
    self.bad_data={
                "first_name":"",
                "last_name":"",
                "date_of_birth":datetime.date(1996,2,28),
                "registration_number":"xyz",
                "place_of_residence":"Kenya",
                "email":"",
                "phone_number":"00007092354",
                "guardian_name":"Jane Muthami",
                "ID_Number":"234333",
                # "DateJoined":datetime.date(2019,1,11),


    }

        

    def test_student_form_validate_data(self):
        form=StudentForm(self.data)
        self.assertTrue(form.is_valid())

    def test_student_rejects_invalid_data(self):
        form=StudentForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_student_test(self):
        url=reverse("add_student")
        request=client.post(url,self.data)
        self.assertEqual(request.status_code,300)

    def test_add_student_test_baddata(self):
        url=reverse("add_student")
        request=client.post(url,self.data)
        self.assertEqual(request.status_code,400)