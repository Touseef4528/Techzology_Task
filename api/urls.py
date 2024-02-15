# your_app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('task/', views.create_task, name='create_task'),  # API endpoint for creating a task
    path('tasks/', views.list_tasks, name='list_tasks'),   # API endpoint for listing tasks
]
