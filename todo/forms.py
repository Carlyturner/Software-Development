
from django import forms
from .models import Task

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class TaskForm(forms.ModelForm):
    
    class Meta:
        
        model = Task
        fields = ['title', 'content']



class CreateUserForm(UserCreationForm):

    class meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    









