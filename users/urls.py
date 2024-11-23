"""Defines URL patterns for users"""
from django.urls import path
from . import views

app_name = 'users'  # Optional but good practice for namespaces

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
