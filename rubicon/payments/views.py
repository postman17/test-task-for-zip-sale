import json
import logging
import urllib.parse
from django.views.generic import TemplateView, View
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.utils import timezone

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


@method_decorator(csrf_exempt, name='dispatch')
class OrderNotification(View):
    def post(self, request):
        logger.info(request.body)
        url_params = urllib.parse.parse_qs(request.body.decode())
        merchant_id = url_params.get('MERCHANT_ORDER_ID')[0] if len(url_params.get('MERCHANT_ORDER_ID')) > 0 else 0
        if merchant_id:
            order = models.Order.objects.filter(id=merchant_id).first()
            if order:
                order.status = models.Order.STATUS_SUCCESS
                order.updated_at = timezone.now()
                order.save(update_fields=['status', 'updated_at'])

        return HttpResponse('YES')


class FormOfPayment(TemplateView):
    template_name = 'payments/form_of_payment.html'
