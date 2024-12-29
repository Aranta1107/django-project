from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .forms import AddStudent
# Create your views here.
from .models import User
def addStudent(request):
    if request.method=='POST':
        fm=AddStudent(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm, email=em, password=pw)
            reg.save()
            fm= AddStudent()
    else:
        fm= AddStudent()
    studentList= User.objects.all()
    return render(request, 'add.html', {'form':fm, 'stuList':studentList})


def deleteStudent(request, id):
    if request.method=='POST':
        reg=User.objects.get(pk=id)
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