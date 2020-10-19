from django.urls import path

from . import views


urlpatterns = [
    path('success/', views.SuccessPage.as_view()),
    path('failed/', views.FailedPage.as_view()),
    path('get_payment_url/', views.PaymentUrl.as_view()),
    path('order_notification/', views.OrderNotification.as_view()),
    path('form_of_payment/', views.FormOfPayment.as_view()),
]
