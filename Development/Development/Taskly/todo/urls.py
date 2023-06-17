from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('', views.home, name="home"),
    path('create-task', views.createTask, name="create-task"),
    path('view-task', views.viewTask, name="view-task"),
    path('update-task/<str:pk>/', views.updateTask, name="update-task"),
    path('delete-task/<str:pk>/', views.deleteTask, name="delete-task"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user-logout', views.user_logout, name="user-logout"),
]










