from celery import shared_task
from .models import Task

@shared_task
def process_task(task_id):
    print("Task processing started")
    # Retrieve the task object using the provided task_id
    task = Task.objects.get(id=task_id)
    print(task)

    task.status = 'Processed'
    task.save()
    print("Task processing completed")

@shared_task
def print_task_name(task_name):
    print("Scheduled task executed:")
    print(task_name)
