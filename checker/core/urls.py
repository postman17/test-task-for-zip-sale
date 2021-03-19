from django.urls import path
from .views import IndexView, ResultView


app_name = 'core'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('result/', ResultView.as_view(), name='result')
]
