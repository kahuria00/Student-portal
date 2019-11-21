from django.test import TestCase
from student.models import Student
from course.models import Course
from teacher.models import Teacher

import datetime



class StudentCourseTeacherTestCase(TestCase):
    def setUp(self):
        self.student_a=Student.objects.create(
            first_name="Cherrie",
            last_name="Wanja",
            date_of_birth=datetime.date(1996,2,28),
            registration_number="xyz",
            place_of_residence="Kenya",
            phone_number="00007092354",
            email="charity@yahoo.com",
            guardian_name="namely guardian",
            ID_Number="234333",
            DateJoined=datetime.date(2019,2,1),

)
        self.student_b=Student.objects.create(
            first_name="Chatto",
            last_name="Grace",
            date_of_birth=datetime.date(1996,8,29),
            registration_number="xyz",
            place_of_residence="US",
            phone_number="0709234981",
            email="challo@yahoo.com",
            guardian_name="namely angel",
            ID_Number="2343369",
            DateJoined=datetime.date(2019,2,1),

)
        self.python =Course.objects.create(
           courseName="python",
           duration_in_month="4",
           courseNumber="667765",
           course_description="data",
           )
        self.business=Course.objects.create(
           courseName="Business Development",
           duration_in_month="8",
           courseNumber="667705",
           course_description="we develop business",
           )
        self.hardware=Course.objects.create(
            courseName="Hardware Design",
            duration_in_month="4",
            courseNumber="667784",
            course_description="Hardware repairs"
           )
        self.teacher_a=Teacher.objects.create(
            first_name="charity",
            last_name="Wanjiru",
            registration_number="6677865",
            place_of_residence="Kilimani",
            phone_number="070010523",
            email="charie@gmail.com",
            ID_Number="987768787",
            DateJoined=datetime.date.today(),
            profession="BackendDeveloper",
            )
        self.teacher_b=Teacher.objects.create(
            first_name="Felister",
            last_name="Chesang",
            registration_number="127865",
            place_of_residence="Kilimani",
            phone_number="0720203016",
            email="chessie@gmail.com",
            ID_Number="98772327",
            DateJoined=datetime.date.today(),
            profession="DataScientist",
            )
    def test_student_can_join_many_courses(self):
        self.assertEqual(self.student_a.courses.count(),0)
        self.student_a.courses.add(self.python)
        self.assertEqual(self.student_a.courses.count(),1)
        self.student_a.courses.add(self.hardware)
        self.assertEqual(self.student_a.courses.count(),2)
        self.student_a.courses.add(self.business)
        self.assertEqual(self.student_a.courses.count(),3)
    
    

    def test_courses_can_have_many_students(self):
        self.python.students.add(self.student_a,self.student_b)
        self.assertEqual(self.python.students.count(),2)

    def test_teacher_can_have_many_courses(self):
        self.python.teacher = self.teacher_a
        self.assertEqual(self.python.teacher.first_name,"charity")
        self.hardware.teacher = self.teacher_a
        self.assertEqual(self.hardware.teacher.first_name,"charity")

        
        
    def test_course_cannot_have_many_teachers(self):
        self.python.teacher = self.teacher_a
        self.hardware.teacher = self.teacher_b
        self.assertEqual(self.python.teacher.first_name,"charity")
        self.assertEqual(self.hardware.teacher.first_name,"Felister")

    def test_course_teacher_is_in_student_teacher_list(self):
        self.python.teacher=self.teacher_a
        self.student_a.courses.add(self.python)
        teachers=self.student_a.teacher()
        self.assertTrue(self.teacher_a in teacher)



