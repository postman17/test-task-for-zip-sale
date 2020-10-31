import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = os.getenv('BROKER_URI')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'Clear not confirmation orders': {
        'task': 'payments.tasks.clear_not_confirmation_orders',
        'schedule': crontab(minute='*/10'),
    },
    'Remove expired data users from whitelist': {
        'task': 'core.tasks.whitelist_handler',
        'schedule': crontab(minute=0, hour='*/1'),
    },
}
