import os 
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoU5.settings')
app = Celery('ProyectoU5')
app.config_from_object("django.conf:settings", namespace='CELERY')


app.conf.beat_schedule = {
    'add-every-1-minute':{
        'task':'payment.tasks.create_payment_expired',
        'schedule':crontab(hour=0),        
    }
}
app.autodiscover_tasks()
app.conf.timezone="America/Lima"