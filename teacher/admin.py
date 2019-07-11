from django.contrib import admin
from .models import Teacher
class TeacherAdmin(admin.ModelAdmin):
	list_display=("first_name","last_name","registration_number","email","profession")
	search_fields=("registration_number","email","last_name","image")
	list_filter=("DateJoined","email")

admin.site.register(Teacher,TeacherAdmin)


# Register your models here.
