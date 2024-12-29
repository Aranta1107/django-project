from django.core import validators
from django import forms 
from .models import Student, Teacher


class AddStudent(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name', 'email', 'password', 'dob']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher', None)
        super().__init__(*args, **kwargs)
        if teacher:
            self.instance.teacher = teacher    
        
class TeacherRegistration(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['username', 'email','password']
        widgets ={
            'usernamename':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            
        }
        
        
class TeacherLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))