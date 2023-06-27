
from django import forms
from .models import Task

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from . models import Task, Profile


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = ['title', 'content']
        exclude = ['user']


#update a user 

class UpdateUserForm(forms.ModelForm):

    password = None

    class Meta:

        model = User 
        fields = ['username', 'email']
        exclude = ['password1', 'password2']

    

#update a profile pic

class updateProfileForm(forms.ModelForm):

    profile_pic= forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))

    class Meta:

        model = Profile
        fields = ['profile_pic',]







