from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('task_name','created_at')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)  # Make the created_at field read-only