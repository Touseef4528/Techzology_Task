from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # ForeignKey relationship with User model 
    task_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
