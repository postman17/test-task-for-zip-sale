from decimal import Decimal
from django.db import models
from django.conf import settings


class Privilege(models.Model):
    """Server users privileges."""

    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    comment = models.TextField(default="", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'payments__privileges'
        indexes = (
            models.Index(fields=['name']),
        )

    def __str__(self):
        return f'{self.name} - {str(self.amount)} рублей - {self.comment}'


class Order(models.Model):
    """Free kassa order."""

    STATUS_NEW = 'NEW'
    STATUS_IN_PROGRESS = 'IN_PROGRESS'
    STATUS_SUCCESS = 'SUCCESS'
    STATUS_FAILED = 'FAILED'
    STATUS_CHOICES = (
        (STATUS_NEW, 'New'),
        (STATUS_IN_PROGRESS, 'In progress'),
        (STATUS_SUCCESS, 'Success'),
        (STATUS_FAILED, 'Failed'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    privilege = models.ForeignKey('Privilege', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    nickname = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    updated_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'payments__orders'
        indexes = (
            models.Index(fields=['nickname']),
        )

    def __str__(self):
        return f'{self.nickname} - {self.amount}'
