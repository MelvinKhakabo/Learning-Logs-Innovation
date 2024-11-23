from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('topics/new/', views.new_topic, name='new_topic'),  # Ensure this is correct
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('', views.index, name='index'), 
    path('users/login/', views.login_view, name='login'), 
    path('users/logout/', views.logout_view, name='logout'),
    path('users/register/', views.register, name='register'),
]

