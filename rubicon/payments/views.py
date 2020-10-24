import json
import logging
from django.views.generic import TemplateView, View
from django.http import JsonResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from . import services


logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/opt/app/log/orders_webhook.log')
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
            nickname = body['nickname'].strip()
            privilege_id = body['privilege_id']
        except Exception:
            raise Http404

        url = services.get_payment_url(privilege_id, nickname)
        return JsonResponse({'url': url})


@method_decorator(csrf_exempt, name='dispatch')
class OrderNotification(View):
    def post(self, request):
        logger.info(request.body)
        services.order_notification_handler(request.body.decode())

        return HttpResponse('YES')


class FormOfPayment(TemplateView):
    template_name = 'payments/form_of_payment.html'
