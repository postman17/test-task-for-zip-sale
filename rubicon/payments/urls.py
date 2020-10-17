from django.urls import path, include

from . import views


urlpatterns = [
    path('success/', views.SuccessPage.as_view()),
    path('failed/', views.FailedPage.as_view()),
]
