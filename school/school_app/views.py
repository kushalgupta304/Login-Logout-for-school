from django.shortcuts import render, redirect

from school_app.forms import LoginForm, RegisterStudent, RegisterTeacher
from .models import Student,Teacher

# Create your views here.
def student_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = Student.objects.filter(email=email, password=password)

            if len(user) >=1:
                return render(request,'dashboard.html', {'name':user[0].name})
            else:
                return render(request, 'dashboard.html', {'name':"Looks like you entered the wrong credentials!!!"})
        else:
            return render(request, 'dashboard.html', {'name':"Looks like you entered the wrong credentials!!!"})

        
    login_form = LoginForm()
    return render(request, 'student_login.html',{'login_form':login_form})

def teacher_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = Teacher.objects.filter(email=email, password=password)

            if len(user) >=1:
                return render(request,'dashboard.html', {'name':user[0].name})
            else:
                return render(request, 'dashboard.html', {'name':"Looks like you entered the wrong credentials!!!"})
        else:
            return render(request, 'dashboard.html', {'name':"Looks like you entered the wrong credentials!!!"})

    login_form = LoginForm()
    return render(request, 'teacher_login.html', {'login_form':login_form})

def register_teacher(request):
    if request.method == 'POST':
        register_form = RegisterTeacher(request.POST)
        if register_form.is_valid():
            register_form.save()
            return render(request,'dashboard.html', {'name' : 'successfully registered'})
        else:
            return render(request,'dashboard.html', {'name' : 'Unsuccessful regiistration'}) 
    
    register_form = RegisterTeacher()
    return render(request, 'teacher_register.html', {'register_form':register_form})

def register_student(request):
    if request.method == 'POST':
        register_form = RegisterStudent(request.POST)
        if register_form.is_valid():
            register_form.save()
            return render(request,'dashboard.html', {'name' : 'successfully registered'})
        else:
            return render(request,'dashboard.html', {'name' : 'Unsuccessful regiistration'}) 
    
    register_form = RegisterStudent()
    return render(request, 'student_register.html', {'register_form':register_form})

def dashboard_page(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'home.html')