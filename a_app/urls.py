from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.addStudent, name='addStudent'),
    path('delete/<int:id>', views.deleteStudent, name='deleteStudent'),
    path('<int:id>', views.updateStudent, name='updateStudent')
]