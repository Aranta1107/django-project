from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from .forms import AddStudent, TeacherRegistration, TeacherLoginForm
from django.contrib import messages
from .models import Student, Teacher
# Create your views here.
def addStudent(request):
    teacher_id=request.session.get('teacher_id')
    teacher_name=request.session.get('teacher_name')
    teacher=Teacher.objects.get(id=teacher_id)
    if request.method=='POST':
        fm=AddStudent(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            do=fm.cleaned_data['dob']
            reg=Student(name=nm, email=em, password=pw, dob=do)
            reg.teacher=teacher
            reg.save()
            fm= AddStudent()
    else:
        intial_data={'name':'', 'email':'', 'password':'', 'dob':''}
        fm= AddStudent(initial=intial_data)
    studentList= Student.objects.filter(teacher=teacher)
    return render(request, 'add.html', {'form':fm, 'stuList':studentList, 'teacher':teacher_name})


def deleteStudent(request, id):
    if request.method=='POST':
        reg=Student.objects.get(pk=id)
        reg.delete()
    return HttpResponseRedirect('/')


def updateStudent(request, id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=AddStudent(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=AddStudent(instance=pi)
    return render(request, 'update.html', {'form':fm})


def register_teacher(request):
    if request.method=='POST':
        fm=TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Registration successful!")
            return redirect('login_teacher')
    else:
        fm=TeacherRegistration()
    return render(request, 'register_teacher.html', {'fm':fm})
    
            
def login_teacher(request):
    if request.method=='POST':
        fm= TeacherLoginForm(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
            try:
                teacher=Teacher.objects.get(username=username, password=password)
                request.session['teacher_id']=teacher.id
                request.session['teacher_name']=teacher.username
                return redirect('addStudent')
            except Teacher.DoesNotExist:
                messages.error(request, "Invalid username or password")
    else:
        fm=TeacherLoginForm()
    return render(request, 'login_teacher.html', {'fm':fm})


def logout_teacher(request):
    request.session.flush()
    return redirect('login_teacher')
