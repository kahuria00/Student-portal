from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
	list_display=("first_name","last_name","registration_number","email","DateJoined")
	search_fields=("registration_number","email","last_name","image")
	list_filter=("DateJoined","date_of_birth")
admin.site.register(Student,StudentAdmin)


# Register your models here.
