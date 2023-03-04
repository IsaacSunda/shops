from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from store.models import Category, Product, Cart, CartItem, Transaction, Order
from store.serializer.store_serializer import CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer, \
    TransactionSerializer, OrderSerializer


# Create your views here.

class CategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CartView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class TransactionView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class OrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


