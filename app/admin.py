from django.contrib import admin
from .models import Student_form,Course_form,Professor_form

# Register your models here.

@admin.register(Student_form)
class Student_formAdmin(admin.ModelAdmin):
    list_display =('Hall_ticket_number','First_name','Last_name','Mobile','Email','Username',)

@admin.register(Course_form)
class Course_formAdmin(admin.ModelAdmin):
    list_display =('Course_name','Semester','Start_date','End_date')

@admin.register(Professor_form)
class Professor_formAdmin(admin.ModelAdmin):
    list_display =('prof_id','First_name','Last_name','Prof_username','Contact_number')
        

