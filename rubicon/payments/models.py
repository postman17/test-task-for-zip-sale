from decimal import Decimal
from django.db import models


class Privilege(models.Model):
    """Server users privileges."""

    name = models.CharField(max_length=200)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00')
    )
    comment = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'payments__privileges'
        indexes = (
            models.Index(fields=['name']),
        )

    def __str__(self):
        return f'{self.name} - {str(self.amount)} рублей - {self.comment}'

