import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')


app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = os.getenv('BROKER_URI')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    # 'Tracking proxies': {
    #     'task': 'tracker.tasks.tracking',
    #     'schedule': crontab(minute=0, hour=0, day_of_month='*/3'),
    # },
    # 'Upload proxies': {
    #     'task': 'tracker.tasks.proxy_uploader',
    #     'schedule': crontab(minute=0, hour='*/1'),
    # },
}
