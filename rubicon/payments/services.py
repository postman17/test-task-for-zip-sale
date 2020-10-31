import hashlib
import urllib.parse
from django.http import Http404
from django.conf import settings
from django.utils import timezone


def get_payment_url(privilege_id, nickname):
    """Get computed payment url."""
    from .models import Privilege, Order

    privilege = Privilege.objects.filter(id=privilege_id, is_active=True).first()
    if not privilege:
        raise Http404

    order = Order.objects.create(
        privilege=privilege,
        nickname=nickname,
        amount=privilege.amount
    )
    merchant_id = settings.MERCHANT_ID
    sign = hashlib.md5(f'{merchant_id}:{privilege.amount}:{settings.SECRET_WORD_1}:{order.id}'.encode())
    return f'/payments/form_of_payment?merchant_id={merchant_id}&amount={privilege.amount}&' \
           f'order_id={order.id}&sign={sign.hexdigest()}'


def order_notification_handler(url_data):
    """Order webhook handler."""
    from .models import Order
    from core.models import WhiteList

    url_params = urllib.parse.parse_qs(url_data)
    merchant_id = url_params.get('MERCHANT_ORDER_ID')[0] if len(url_params.get('MERCHANT_ORDER_ID')) > 0 else 0
    if merchant_id:
        order = Order.objects.filter(id=merchant_id).first()
        if order:
            order.status = Order.STATUS_SUCCESS
            order.updated_at = timezone.now()
            order.save(update_fields=['status', 'updated_at'])
            whitelist_record = WhiteList.objects.create(
                expire_at=timezone.now() + timezone.timedelta(days=30),
                nickname=order.nickname,
            )
            whitelist_record.add_to_whitelist()
