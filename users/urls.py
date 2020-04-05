"""Defines URL patterns for users"""
from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
	# Include default auth urls.
    # http://localhost:8000/users/login/ (users.urls.py & login view)
	path('', include('django.contrib.auth.urls')),
    # Registration page.
    # http://localhost:8000/users/register/
	path('register/', views.register, name='register'),
]
