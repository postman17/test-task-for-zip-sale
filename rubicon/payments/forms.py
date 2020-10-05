from django import forms

from .models import Privilege


class BuyingPrivilegeForm(forms.Form):
    """Buying privileges form."""

    privilege = forms.ModelChoiceField(
        queryset=Privilege.objects.all(), required=True, label=''
    )
    privilege.widget.attrs.update(
        {'style': 'display: block;', 'class': 'privilege'}
    )
