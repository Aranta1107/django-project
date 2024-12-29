from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register_teacher, name='register_teacher'),
    path('login', views.login_teacher, name='login_teacher'),
    path('logout', views.logout_teacher, name='logout'),
    path('addStudent', views.addStudent, name='addStudent'),
    path('delete/<int:id>', views.deleteStudent, name='deleteStudent'),
    path('<int:id>', views.updateStudent, name='updateStudent')
]