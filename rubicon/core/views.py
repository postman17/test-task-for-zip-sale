from django.views.generic import FormView

from payments.forms import BuyingPrivilegeForm


class IndexView(FormView):
    """Display index page."""
    form_class = BuyingPrivilegeForm
    template_name = 'core/index.html'
