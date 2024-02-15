from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Task
from .tasks import process_task


@login_required
def index(request):
    print(request.user)
    return render(request, 'home.html')


def login_view(request):
    print('Enter')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to a Home
        else:
            return HttpResponse("Invalid username or password. Please try again.")
    else:
        return render(request, 'login.html')


@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        user = request.user
        task_name = request.POST.get('task_name')
        current_time = datetime.now()  # Set current time on which task should submitted
        data = Task(user=user, task_name=task_name, created_at=current_time)
        data.save()

        # Trigger Celery task asynchronously
        process_task.delay(data.id)
        print("This is the testing process", process_task.delay(data.id))

        response_data = {
            'task_name': task_name,
            'current_time': str(current_time),  # Convert to string
            'message': 'Task created successfully!',
        }

        return JsonResponse(response_data)
    else:
        return render(request, 'create_task.html')


def list_tasks(request):
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user)
        return render(request, 'list_tasks.html', {'tasks': tasks})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
