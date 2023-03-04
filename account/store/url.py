from django.urls import path

from store.views import CategoryView, ProductView, CartView, CartItemView, TransactionView, OrderView

urlpatterns = [
    path('category', CategoryView.as_view()),
    path('product', ProductView.as_view()),
    path('cart', CartView.as_view()),
    path('cart/item', CartItemView.as_view()),
    path('transaction', TransactionView.as_view()),
    path('order', OrderView.as_view()),
]