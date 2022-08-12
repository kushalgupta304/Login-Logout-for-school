from unicodedata import name
from django import forms
from django.forms import ModelForm
from .models import Student, Teacher

class RegisterStudent(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"name",
            'label':''
            }
        ), label='',
        required=True)

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"password",
            'label':''
            }
        ), label='',
        required=True)

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"email",
            'label':''
            }
        ), label='',
        required=True)

    standard = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"standard",
            'label':''
            }
        ), label='',
        required=True)
    
    section = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"section",
            'label':''
            }
        ), label='',
        required=True)

    stream = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"stream",
            'label':''
            }
        ), label='',
        required=True)

    roll_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"roll_number",
            'label':''
            }
        ), label='',
        required=True)
    class Meta:
        model = Student
        fields = '__all__'

class RegisterTeacher(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"name",
            'label':''
            }
        ), label='',
        required=True)

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"password",
            'label':''
            }
        ), label='',
        required=True)

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"email",
            'label':''
            }
        ), label='',
        required=True)

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"subject",
            'label':''
            }
        ), label='',
        required=True)
    
    classes_taught = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"classes_taught",
            'label':''
            }
        ), label='',
        required=True)
    
    contact_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"contact_number",
            'label':''
            }
        ), label='',
        required=True)
    class Meta:
        model = Teacher
        fields = '__all__'

class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
            'class':"login-input",
            'placeholder':"email",
            'label':''
            }
        ), label='',
        required=True)
    password = forms.CharField(
        widget = forms.TextInput(
            attrs={
                'class':'login-input',
                'placeholder':'password',
                'label':''
            }
        ),label='',
        required=True)