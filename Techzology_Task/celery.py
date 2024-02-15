from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Techzology_Task.settings')

app = Celery('Techzology_Task')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Use Redis as a Broker Like we can say Broker Message
app.conf.broker_url = 'redis://localhost:6379/0'

app.conf.beat_schedule = {
    'print-task-name-every-10-seconds': {
        'task': 'api.tasks.print_task_name',
        'schedule': 10,  # Execute every 10 seconds
        'args': ('Techzology_Task',) 
    },
}

app.autodiscover_tasks()

# This is just a simple example as was mentioned in the task, but through Celery we can make Lots of Operation through
# which our Website could be more efficient and scalable.

# a Simple examples of this is Email OTP systems, WHatsapp OTP systems,

# As in the Email OTP system, we wait on the form page on the submission of the waiting to send email and the page
# loads continuously, but through celery we can make it as the sending email on background and we can move to the next page
# Like OTP verificatioon page, same for whatsapp OTP,

# THis was just a simple examples of use cases of celery
