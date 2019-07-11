from django.contrib import admin
from .models import Course
class CourseAdmin(admin.ModelAdmin):
	list_display=("courseName","course_description","courseNumber","duration_in_month","teacher")
	search_fields=("courseName","courseNumber","teacher__email","teacher__first_name","teacher__registration_number")
	list_filter=("teacher__first_name",)

admin.site.register(Course,CourseAdmin)

# Register your models here.
