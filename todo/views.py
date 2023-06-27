
from django.shortcuts import render, redirect
from django.http import HttpResponse 

from .models import Task, Profile
from .forms import CreateTaskForm, TaskForm, CreateUserForm, LoginForm, CreateUserForm, UpdateUserForm

from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from .models import Task, Profile

from django.contrib.auth.models import User

from django.contrib import messages 

from todo.forms import updateProfileForm

from django.utils import timezone




# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required  # Use the login_required decorator to ensure a user is logged in
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            current_user = form.save(commit=False)

            form.save()

            profile = Profile.objects.create(user=current_user)

            
            messages.success(request, "User registration was succesful!")

            return redirect("my-login")

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



#dashboard
@login_required(login_url='my-login')
def dashboard(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    
    context = {'profile': profile}
    return render(request, 'profile/dashboard.html', context=context)





def home(request):
    return render(request, 'index.html')


#profile-management
@login_required(login_url='my-login')
def profile_management(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    
    user_form = UpdateUserForm(instance=request.user)
    form_2 = updateProfileForm(instance=profile)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        form_2 = updateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid():
            user_form.save()
            return redirect('dashboard')

        if form_2.is_valid():
            form_2.save()
            return redirect('dashboard')

    context = {'user_form': user_form, 'form_2': form_2}
    return render(request, 'profile/profile-management.html', context=context)



@login_required(login_url='my-login')
def deleteAccount(request):


    if request.method =='POST':
        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect('home')

    return render(request, 'profile/delete-account.html')




#Create Task
@login_required(login_url='my-login')
def createTask(request):
    form = CreateTaskForm()

    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.created_at = timezone.now()  # Set the creation time
            task.save()
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'profile/create-task.html', context=context)


#View To-Do List
#@login_required(login_url='my-login')
#def viewTask(request):
 #   current_user = request.user.id
  #  task = Task.objects.all().filter(user=current_user)
   # return render(request, 'view-task.html', context=context)

#Update Task
@login_required(login_url='my-login')
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

#View all task page 


@login_required(login_url='my-login')
def viewTask(request):
    current_user = request.user.id
    task = Task.objects.all().filter(user=current_user)
    context = {'task': task}

    return render(request, 'profile/view-task.html', context=context)
                  


from django.shortcuts import render

def login_view(request):
    # Your login view implementation here
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            current_user = form.save(commit=False)

            form.save()

            profile = Profile.objects.create(user=current_user)

            
            messages.success(request, "User registration was succesful!")

            return redirect("my-login")

    context = {'form': form}
    return render(request, 'register.html', context=context)
    
