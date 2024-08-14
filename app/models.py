from django.db import models
from django.urls import reverse

# Create your models here.
class Student_form(models.Model):

    GENDER_CHOICES = [('male', 'Male'),('female', 'Female'),('other', 'Other'),]
    COURSE_CHOICES = [('CS', 'Computer Science'),('IT', 'Information Technology'),('ECE', 'Electronics and Communication Engineering'),('ME', 'Mechanical Engineering'),]
    CURRENT_COURSE = [('CYS', 'Cyber Security'),('DS', 'Data Science'),('CS', 'Computer Science')]

    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    Date_of_birth = models.DateField()
    Email = models.EmailField()
    Mobile = models.CharField(max_length=10)
    Father_name = models.CharField(max_length=50)
    Occupation = models.CharField(max_length=50, blank=True, null=True)
    Hall_ticket_number = models.CharField(max_length=10)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=12)
    Highest_graduation = models.CharField(max_length=50)
    Year_of_passout = models.CharField(max_length=4)
    Specialization = models.CharField(max_length=50,choices=COURSE_CHOICES)
    Percentage = models.DecimalField(max_digits=5, decimal_places=2)
    College_name = models.CharField(max_length=200)
    College_website = models.URLField()
    College_code = models.CharField(max_length=4)
    IELTS_GRE_score = models.DecimalField(max_digits=3, decimal_places=1)
    Current_course = models.CharField(max_length=100,choices=CURRENT_COURSE)
    Enroll_date = models.DateField()
    Course_duration = models.CharField(max_length=50)
    Address = models.TextField()
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Pincode = models.CharField(max_length=6)
    Country = models.CharField(max_length=30)
    Guardian_name = models.CharField(max_length=50)
    Guardian_relation = models.CharField(max_length=50)
    Guardian_contact = models.CharField(max_length=15)
    Guardian_email = models.EmailField()
    Present_address = models.TextField()    

    class Meta:
        verbose_name = ("Student_form")
        verbose_name_plural = ("Student_forms")

    def __str__(self):
        return self.Hall_ticket_number

    def get_absolute_url(self):
        return reverse("Student_form_detail", kwargs={"pk": self.pk})

class Course_form(models.Model):

    COURSE_CHOICES = [('Data Science1', 'Data Science1'),('Data Science2', 'Data Science2'),('Computer Science1', 'Computer Science1'),('Computer Science2', 'Computer Science2'),('Cyber Security1', 'Cyber Security1'),('Cyber Security2', 'Cyber Security2'),]
    SEMESTER_CHOICES = [('semester1', 'Semester 1'),('semester2', 'Semester 2'),('semester3', 'Semester 3'),('semester4', 'Semester 4'),]

    Course_name = models.CharField(max_length=50, choices=COURSE_CHOICES)
    Semester = models.CharField(max_length=50, choices=SEMESTER_CHOICES)
    Subject1 = models.CharField(max_length=100)
    Subject_code1 = models.CharField(max_length=20)
    Credits1 = models.PositiveIntegerField()
    Subject2 = models.CharField(max_length=100)
    Subject_code2 = models.CharField(max_length=20)
    Credits2 = models.PositiveIntegerField()
    Subject3 = models.CharField(max_length=100)
    Subject_code3 = models.CharField(max_length=20)
    Credits3 = models.PositiveIntegerField()
    Subject4 = models.CharField(max_length=100, blank=True, null=True)
    Subject5 = models.CharField(max_length=100, blank=True, null=True)
    Subject6 = models.CharField(max_length=100, blank=True, null=True)
    Course_description = models.TextField()
    Start_date = models.DateField()
    End_date = models.DateField()

    class Meta:
        verbose_name = ("Course_form")
        verbose_name_plural = ("Course_forms")

    def __str__(self):
        return self.Course_name

    def get_absolute_url(self):
        return reverse("Course_form_detail", kwargs={"pk": self.pk})


class Professor_form(models.Model):
  
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Contact_number = models.CharField(max_length=10)
    Email = models.EmailField(max_length=100)
    prof_id = models.CharField(max_length=50)
    Prof_username = models.CharField(max_length=50)
    Prof_password = models.CharField(max_length=128)
    Address = models.TextField()
    Highest_degree = models.CharField(max_length=100)
    Year_of_graduation = models.IntegerField()
    Qualification = models.CharField(max_length=100)
    Experience = models.CharField(max_length=100)
    Previous_position = models.CharField(max_length=100)
    Previous_organization = models.CharField(max_length=100)
    Current_position = models.CharField(max_length=100)
    Teaching_subjects = models.CharField(max_length=100)

    class Meta:
        verbose_name = ("Professor_form")
        verbose_name_plural = ("Professor_forms")

    def __str__(self):
        return f'{self.Last_name} {self.First_name}'

    def get_absolute_url(self):
        return reverse("Professor_form_detail", kwargs={"pk": self.pk})

    