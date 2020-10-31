from mcrcon import MCRcon
from django.db import models
from django.conf import settings


class WhiteList(models.Model):
    """Minecraft server whitelist."""

    STATUS_ACTIVE = 'ACTIVE'
    STATUS_EXPIRED = 'EXPIRED'

    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_EXPIRED, 'Expired'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    nickname = models.CharField(max_length=100)
    expire_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'core__whitelist'
        verbose_name = 'WhiteList'
        verbose_name_plural = 'WhiteList'
        indexes = (
            models.Index(fields=['nickname']),
            models.Index(fields=['status']),
        )

    def __str__(self):
        return f'{self.nickname} - {str(self.expire_at) if self.expire_at else ""}'

    def add_to_whitelist(self):
        """Add user to whitelist."""
        server_ip = settings.RCON_SERVER_IP
        server_secret = settings.RCON_SERVER_SECRET
        with MCRcon(server_ip, server_secret) as mcr:
            mcr.command(f'whitelist add {self.nickname}')

    def remove_from_whitelist(self):
        """Remove user from whitelist."""
        server_ip = settings.RCON_SERVER_IP
        server_secret = settings.RCON_SERVER_SECRET
        with MCRcon(server_ip, server_secret) as mcr:
            mcr.command(f'whitelist remove {self.nickname}')
