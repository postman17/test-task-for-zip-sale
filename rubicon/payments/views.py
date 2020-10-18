import json
import logging
from django.views.generic import TemplateView, View
from django.http import JsonResponse, Http404

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

        return JsonResponse({})
