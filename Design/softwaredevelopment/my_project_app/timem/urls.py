from django.urls import path
from . import views

urlpatterns = [
    path('timem/', views.timem, name='timem'),
]