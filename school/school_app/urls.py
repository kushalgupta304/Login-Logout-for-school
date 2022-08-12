from django.urls import path
from .views import register_student, student_login,teacher_login, register_teacher, home

urlpatterns = [
    path('student_login/', student_login),
    path('teacher_login/', teacher_login),
    path('register_teacher/', register_teacher),
    path('register_student/', register_student),
    path('home/', home),

    

]
