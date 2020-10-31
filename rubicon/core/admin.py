from django.contrib import admin

from . import models


@admin.register(models.WhiteList)
class WhiteListAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
        'expire_at',
    )
    list_filter = (
        'created_at',
        'expire_at',
    )
    search_fields = (
        'nickname',
        'user__username',
    )
    list_display = (
        'id',
        'status',
        'user',
        'nickname',
        'expire_at',
        'created_at',
    )
