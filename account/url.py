from django.urls import path

from account.views import CreateUser, AddressView, PaymentView, AddressUpdateView, UpdatePaymentView, ListPaymentDetail, SingleAddressDetail

urlpatterns = [
    path('user', CreateUser.as_view()),
    path('address', AddressView.as_view()),
    path('payment', PaymentView.as_view()),
    path('payment/update/<int:pk>', UpdatePaymentView.as_view()),
    path('address/update/<int:pk>', AddressUpdateView.as_view()),
    path('payment/list', ListPaymentDetail.as_view()),
    path('address/single/<int:pk>', SingleAddressDetail.as_view())
]