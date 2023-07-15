import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "les_16.settings")
app = Celery("les_16")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
