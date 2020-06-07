from django.contrib import admin

from . import models


@admin.register(models.Privilege)
class PrivilegeAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
    )
    list_filter = (
        'created_at',
    )
    search_fields = (
        'name',
    )
    list_display = (
        'id',
        'name',
        'amount',
        'comment',
        'created_at',
    )
