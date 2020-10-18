import hashlib
from django.http import Http404
from django.conf import settings


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
    sign = hashlib.md5(f'{merchant_id}{settings.SECRET_WORD_1}'.encode())
    return f'/payments/form_of_payment?merchant_id={merchant_id}&amount={privilege.amount}&' \
           f'order_id={order.id}&sign={sign.hexdigest()}'
