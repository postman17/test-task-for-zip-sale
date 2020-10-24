from project.celery import app
from django.utils import timezone

from . import models


@app.task
def clear_not_confirmation_orders():
    """Clear all not confirmation orders."""
    period = timezone.now() - timezone.timedelta(days=1)
    orders = models.Order.objects.filter(status=models.Order.STATUS_NEW, created_at__lte=period)
    orders.delete()
