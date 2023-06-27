from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login_view, name='login'),  # Add this line for login URL pattern
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('my-login/', views.my_login, name='my-login'),
    path('', views.home, name='home'),
    path('create-task/', views.createTask, name='create-task'),
    path('view-task/', views.viewTask, name='view-task'),
    path('update-task/<str:pk>/', views.updateTask, name='update-task'),
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile-management/', views.profile_management, name='profile-management'),
    path('delete-account/', views.deleteAccount, name='delete-account'),
    path('user-logout/', views.user_logout, name='user-logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

