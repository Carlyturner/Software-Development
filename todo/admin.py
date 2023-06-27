from django.contrib import admin

from .models import Task, Review, Profile

# Register your models here.

admin.site.register(Task)

admin.site.register(Review)

admin.site.register(Profile)


