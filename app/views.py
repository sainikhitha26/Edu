from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from .models import *

from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect

def index(request):         
    return render(request,'index.html')

def base(request):
    data1 = Professor_form.objects.all()
    data2 = Student_form.objects.all()
    data3 = Course_form.objects.all()

    First_name = Last_name = Gender = Date_of_birth = Email = Mobile = Father_name = Occupation = Highest_graduation = Year_of_passout = Specialization = Percentage = College_name = College_website = College_code = IELTS_GRE_score = Current_course = Enroll_date = Course_duration = Hall_ticket_number = Username = Password = Address = City = State = Pincode = Country = Guardian_name = Guardian_relation = Guardian_contact = Guardian_email = Present_address = None
    if request.method=='POST':
        First_name = request.POST.get('first-name')
        Last_name = request.POST.get('last-name')
        Gender = request.POST.get('gender')
        Date_of_birth = request.POST.get('dob')
        Email = request.POST.get('email')
        Mobile = request.POST.get('mobile')
        Father_name = request.POST.get('father-name')
        Occupation = request.POST.get('occupation')
        Highest_graduation = request.POST.get('highest-graduation')
        Year_of_passout = request.POST.get('year-of-passout')
        Specialization = request.POST.get('specialization')
        Percentage = request.POST.get('percentage')
        College_name = request.POST.get('college-name')
        College_website = request.POST.get('college-web')
        College_code = request.POST.get('college-code')
        IELTS_GRE_score = request.POST.get('ielts-gre-score')
        Current_course = request.POST.get('current-course')
        Enroll_date = request.POST.get('enroll-date')
        Course_duration = request.POST.get('course-duration')
        Hall_ticket_number = request.POST.get('hall-ticket-number')
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        Address = request.POST.get('address')
        City = request.POST.get('city')
        State = request.POST.get('state')
        Pincode = request.POST.get('pincode')
        Country = request.POST.get('country')
        Guardian_name = request.POST.get('guardian-name')
        Guardian_relation = request.POST.get('guardian-relation')
        Guardian_contact = request.POST.get('guardian-contact')
        Guardian_email = request.POST.get('guardian-mail')
        Present_address = request.POST.get('present-address')

    if First_name and Last_name and Gender and Date_of_birth and Email and Mobile:
        Student_form.objects.create(
            First_name = First_name,
            Last_name = Last_name,
            Gender = Gender,
            Date_of_birth = Date_of_birth,
            Email = Email,
            Mobile = Mobile,
            Father_name = Father_name,
            Occupation = Occupation,
            Highest_graduation = Highest_graduation,
            Year_of_passout = Year_of_passout,
            Specialization = Specialization,
            Percentage = Percentage,
            College_name = College_name,
            College_website = College_website,
            College_code = College_code,
            IELTS_GRE_score = IELTS_GRE_score,
            Current_course = Current_course,
            Enroll_date = Enroll_date,
            Course_duration = Course_duration,
            Hall_ticket_number = Hall_ticket_number,
            Username = Username,
            Password = Password,
            Address = Address,
            City = City,
            State = State,
            Pincode = Pincode,
            Country = Country,
            Guardian_name = Guardian_name,
            Guardian_relation = Guardian_relation,
            Guardian_contact = Guardian_contact,
            Guardian_email = Guardian_email,
            Present_address = Present_address,
        ).save()

    Course_name = Semester = Subject1 = Subject_code1 = Credits1 = Subject2 = Subject_code2 = Credits2 = Subject3 = Subject_code3 = Credits3 = Subject4 = Subject5 = Subject6 = Course_description = Start_date = End_date = None

    if request.method=='POST':
        Course_name = request.POST.get('courseName')
        Semester = request.POST.get('semester')
        Subject1 = request.POST.get('subject1')
        Subject_code1 = request.POST.get('subjectCode1')
        Credits1 = request.POST.get('credits1')
        Subject2 = request.POST.get('subject2')
        Subject_code2 = request.POST.get('subjectCode2')
        Credits2 = request.POST.get('credits2')
        Subject3 = request.POST.get('subject3')
        Subject_code3 = request.POST.get('subjectCode3')
        Credits3 = request.POST.get('credits3')
        Subject4 = request.POST.get('subject4')
        Subject5 = request.POST.get('subject5')
        Subject6 = request.POST.get('subject6')
        Course_description = request.POST.get('courseDescription')
        Start_date = request.POST.get('startDate')
        End_date = request.POST.get('endDate')
    if Course_name and Semester and Subject1 and Subject_code1 and Credits1 and Subject2 and Subject_code2 and Credits2 and Subject3 and Subject_code3 and Credits3:
        Course_form.objects.create(
            Course_name =Course_name, 
            Semester =Semester, 
            Subject1 =Subject1, 
            Subject_code1 =Subject_code1, 
            Credits1 =Credits1, 
            Subject2 =Subject2, 
            Subject_code2 =Subject_code2, 
            Credits2 =Credits2, 
            Subject3 =Subject3, 
            Subject_code3 =Subject_code3, 
            Credits3 =Credits3, 
            Subject4 =Subject4, 
            Subject5 =Subject5, 
            Subject6 =Subject6, 
            Course_description =Course_description, 
            Start_date =Start_date, 
            End_date =End_date, 
        ).save()
    First_name = Last_name = Contact_number = Email = prof_id = Prof_username = Prof_password = Address = Highest_degree = Year_of_graduation = Qualification = Experience = Previous_position = Previous_organization = Current_position = Teaching_subjects = None
 
    if request.method=='POST':
        First_name = request.POST.get('firstName')
        Last_name = request.POST.get('lastName')
        Contact_number = request.POST.get('contact')
        Email = request.POST.get('email')
        prof_id = request.POST.get('profid')
        Prof_username = request.POST.get('profusername')
        Prof_password = request.POST.get('profpassword')
        Address = request.POST.get('address')
        Highest_degree = request.POST.get('highestDegree')
        Year_of_graduation = request.POST.get('yearOfGraduation')
        Qualification = request.POST.get('qualification')
        Experience = request.POST.get('experience')
        Previous_position = request.POST.get('previousPosition')
        Previous_organization = request.POST.get('previousOrganization')
        Current_position = request.POST.get('currentPosition')
        Teaching_subjects = request.POST.get('teachingSubjects')

    if First_name and Last_name and Contact_number and Email and prof_id and Prof_username and Prof_password and Address and Highest_degree and Year_of_graduation and Qualification and Experience and Previous_position and Previous_organization and Current_position and Teaching_subjects:
        Professor_form.objects.create(
            First_name = First_name,
            Last_name = Last_name,
            Contact_number = Contact_number,
            Email = Email,
            prof_id = prof_id,
            Prof_username = Prof_username,
            Prof_password = Prof_password,
            Address = Address,
            Highest_degree = Highest_degree,
            Year_of_graduation = Year_of_graduation,
            Qualification = Qualification,
            Experience = Experience,
            Previous_position = Previous_position,
            Previous_organization = Previous_organization,
            Current_position = Current_position,
            Teaching_subjects = Teaching_subjects,
        ).save()  

        profid = request.GET.get('profid')
        firstName = request.GET.get('firstName')
        lastName = request.GET.get('lastName')
        profusername = request.GET.get('profusername')
        contact = request.GET.get('contact')
        if profid:
            data1 = data1.filter(profid__icontains=profid)        
        if firstName:
            data1 = data1.filter(firstName__icontains=firstName)        
        if lastName:
            data1 = data1.filter(lastName__icontains=lastName)
        if profusername:
            data1 = data1.filter(profusername__icontains=profusername)
        if contact:
            data1 = data1.filter(contact__icontains=contact)

        Hall_ticket_number = request.GET.get('highest-graduation')
        First_name = request.GET.get('first-name')
        Last_name = request.GET.get('last-name')
        Mobile = request.GET.get('mobile')
        Email = request.GET.get('email')
        Username = request.GET.get('username')
        if Hall_ticket_number:
            data2 = data2.filter(Hall_ticket_number__icontains=Hall_ticket_number)
        if First_name:
            data2 = data2.filter(First_name__icontains=First_name)
        if Last_name:
            data2 = data2.filter(Last_name__icontains=Last_name)
        if Mobile:
            data2 = data2.filter(Mobile__icontains=Mobile)
        if Email:
            data2 = data2.filter(Email__icontains=Email)
        if Username:
            data2 = data2.filter(Username__icontains=Username)

        Course_name = request.GET.get('courseName')
        Semester = request.GET.get('semester')
        Start_date = request.GET.get('startDate')
        End_date = request.GET.get('endDate')
        if Course_name:
            data3 = data3.filter(Course_name__icontains=Course_name)
        if Semester:
            data3 = data3.filter(semester__icontains=Semester)
        if Start_date:
            data3 = data3.filter(Start_date__icontains=Start_date)
        if End_date:
            data3 = data3.filter(End_date__icontains=End_date)        

    context={
        'data1': data1,
        'professors': data1,
        'data2': data2,
        'data3': data3,
        }

    return render(request,'base.html',context)


def student_page(request):
    
    data1 = Student_form.objects.all()
    
    context={
        'data1' : data1
    }

    return render(request,'student.html',context)

def aboutus(request):
    return render(request,'aboutus.html')

def baseaboutus(request):
    return render(request,'baseaboutus.html')

def courses(request):
    return render(request,'courses.html')

def events(request):
    return render(request,'events.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def student_login(request):
    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        if username1 and password1:
            try:
                student = Student_form.objects.get(Username=username1)
                if student.Password == password1:
                    # Authentication successful
                    request.session['student_id'] = student.id
                    return redirect('studenthome')
                else:
                    error = 'Invalid username or password'
            except Student_form.DoesNotExist:
                error = 'Invalid username or password'
        else:
            error = 'Username and password are required'

        return render(request, 'studentlogin.html', {'error': error})

    return render(request,'studentlogin.html')

def professor_login(request):       
    if request.method =="POST":
        Prof_username1 = request.POST.get('profusername')
        Prof_password1 = request.POST.get('profpassword')     

        if Prof_username1 and Prof_password1:
            try:
                professor = Professor_form.objects.get(Prof_username = Prof_username1)
                if professor.Prof_password == Prof_password1:
                    request.session['prof_id'] = professor.id
                    return redirect('professorhome')
                else:
                    error = 'Invalid username or password'
            except Professor_form.DoesNotExist:
                error = 'Invalid username or password'
        else:
            error = 'Prof_username and Prof_password are required'

        return render(request,'professorlogin.html',{'error': error})
    
    return render(request,'professorlogin.html')

def admin_login(request):
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('base')   
    return render(request,'adminlogin.html')

def admin_logout(request):
    logout(request)
    return redirect('login')

def student_logout(request):
    logout(request)
    return redirect('login')


def professor_page(request):
    return render(request,'professor.html')


def studenthome(request):
    student_id = request.session.get('student_id')
    if student_id:
        student = Student_form.objects.get(id=student_id)
        return render(request, 'studenthome.html', {'student': student})
    else:
        return redirect('studentlogin')

def professorhome(request):
    prof_id = request.session.get('prof_id')
    if prof_id:
        professor = Professor_form.objects.get(id=prof_id)
        return render(request, 'professorhome.html', {'professor': professor})
    else:
        return redirect('professorlogin')

