from django.views import View
from django.shortcuts import render
from django.http import Http404
from .forms import GitHubUsernameForm
from .services import build_data_to_list


class IndexView(View):
    """Display index page."""

    def get(self, request):
        context = {
            'form': GitHubUsernameForm()
        }
        return render(request, 'core/index.html', context)


class ResultView(View):
    """Display result page."""

    def post(self, request):
        form = GitHubUsernameForm(request.POST)
        if form.is_valid():
            context = {
                'data': build_data_to_list(form.cleaned_data['username'])
            }
            return render(request, 'core/result.html', context)

        raise Http404
