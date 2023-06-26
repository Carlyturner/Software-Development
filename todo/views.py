
from django.shortcuts import render, redirect
from django.http import HttpResponse 

from .models import Task
from .forms import TaskForm, CreateUserForm, LoginForm

from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration Successful!")

    context = {'form': form}
    return render(request, 'register.html', context=context)


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            
    context = {'form': form}
    return render(request, 'my-login.html', context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("home")

@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'index.html')

#Create Task
def createTask(request):
    form = TaskForm()

    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view-task')
        
    context = {'form': form}
    return render(request, 'create-task.html', context=context)

#View To-Do List
def viewTask(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'view-task.html', context=context)

#Update Task
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view-task')

    context = {'form': form}
    return render(request, 'update-task.html', context=context)

#Delete Task
def deleteTask(request, pk): 
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('view-task')

    return render(request, 'delete-task.html')





