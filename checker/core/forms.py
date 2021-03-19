from django import forms


class GitHubUsernameForm(forms.Form):
    """Github username form."""

    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
