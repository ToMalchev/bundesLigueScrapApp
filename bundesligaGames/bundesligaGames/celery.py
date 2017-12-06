from __future__ import absolute_import

import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
import django
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bundesligaGames.settings')
django.setup()
# Load task modules from all registered Django app configs.

app = Celery('bundesligaGames', broker='redis://localhost:6379/')
app.config_from_object('django.conf:settings', namespace='celery')


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'scrape-data': {
        'task': 'bundesLiga.tasks.scrape',
        'schedule': 30 ,  
    },
}
