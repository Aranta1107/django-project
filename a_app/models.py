from django.db import models

# Create your models here.
class Teacher(models.Model):
    username =models.CharField(max_length=70)
    email= models.EmailField(max_length=100)
    password =models.CharField(max_length=100)
    

class Student(models.Model):
    name= models.CharField(max_length=70)
    email= models.EmailField(max_length=100)
    password= models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    teacher=models.ForeignKey(Teacher, related_name='students', on_delete=models.CASCADE)
    
    