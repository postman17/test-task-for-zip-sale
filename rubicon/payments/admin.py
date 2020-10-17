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
        'is_active',
        'created_at',
    )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    list_filter = (
        'created_at',
        'updated_at',
    )
    search_fields = (
        'nickname',
        'user__username',
    )
    list_display = (
        'id',
        'status',
        'privilege',
        'user',
        'nickname',
        'amount',
        'updated_at',
        'created_at',
    )
