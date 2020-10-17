from django.views.generic import TemplateView


class SuccessPage(TemplateView):
    template_name = 'payments/success.html'


class FailedPage(TemplateView):
    template_name = 'payments/failed.html'
