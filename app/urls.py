from django.urls import path
from .views import index,login,aboutus,courses,events,contact,base,baseaboutus,professor_login,student_login,admin_login,studenthome,admin_logout,professorhome,student_logout
urlpatterns = [
    path('',index,name='index'),
    path('base',base,name='base'),
    path('aboutus',aboutus,name='aboutus'),
    path('baseaboutus',baseaboutus,name='baseaboutus'),
    path('courses',courses,name='courses'),
    path('events',events,name='events'),
    path('contact',contact,name='contact'),
    path('signin',login,name='login'),
    path('professorlogin',professor_login,name='professor_login'),
    path('studentlogin',student_login,name='student_login'),
    path('studentlogout',student_logout,name='student_logout'),
    path('adminlogout',admin_logout,name='admin_logout'),
    path('adminlogin',admin_login,name='admin_login'),
    path('studenthome',studenthome,name='studenthome'),
    path('professorhome',professorhome,name='professorhome')
    

]