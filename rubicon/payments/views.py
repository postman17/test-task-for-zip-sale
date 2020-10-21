import json
import logging
from django.views.generic import TemplateView, View
from django.http import JsonResponse, Http404

from . import models
from . import services


logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/opt/app/log/test.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)


class SuccessPage(TemplateView):
    template_name = 'payments/success.html'


class FailedPage(TemplateView):
    template_name = 'payments/failed.html'


class PaymentUrl(View):
    def post(self, request):
        try:
            body = json.loads(request.body)
            nickname = body['nickname']
            privilege_id = body['privilege_id']
        except Exception:
            raise Http404

        url = services.get_payment_url(privilege_id, nickname)
        return JsonResponse({'url': url})


class OrderNotification(View):
    def post(self, request):
        logger.info(request.body)
        try:
            body = json.loads(request.body)
        except Exception:
            raise Http404

        order = models.Order.objects.filter(id=body.get('MERCHANT_ORDER_ID')).first()
        if order:
            order.status = models.Order.STATUS_SUCCESS
            order.updated_at = models.Order.STATUS_SUCCESS
            order.save(update_fields=['status', 'updated_at'])

        raise Exception('YES')


class FormOfPayment(TemplateView):
    template_name = 'payments/form_of_payment.html'
