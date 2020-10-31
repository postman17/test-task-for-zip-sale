from project.celery import app
from django.utils import timezone

from . import models


@app.task
def whitelist_handler():
    """Remove expired date users from whitelist."""
    whitelist_items = models.WhiteList.objects.filter(status=models.WhiteList.STATUS_ACTIVE)
    for whitelist_item in whitelist_items:
        if whitelist_item.expire_at < timezone.now():
            whitelist_item.status = models.WhiteList.STATUS_EXPIRED
            whitelist_item.save(update_fields=['status'])
            whitelist_item.remove_from_whitelist()
