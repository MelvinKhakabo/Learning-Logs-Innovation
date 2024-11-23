"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# learning_log/urls.py
"""URL configuration for learning_log project."""

from django.contrib import admin
from django.urls import path, include
from . import views  # Make sure to import the views module for the home page view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learning_logs/', include('learning_logs.urls', namespace='learning_logs')),
    path('users/', include('users.urls', namespace='users')),  # Include the users app URLs
    path('', views.home_view, name='home'),  # Add this line for the home page URL
]

# learning_logs/urls.py
from django.urls import path
from users import views as user_views  # Import views from the 'users' app as 'user_views'

urlpatterns = [
    # Other paths...
    path('users/login/', user_views.login_view, name='login'),  # Use user_views.login_view
    # Other paths...
]




