from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from cart.serializers import CartSerializers, CartItemSerializers
from account.permission import IsBuyer
from cart.models import Cart,CartItems
from account.models import CustomUser

# ViewSet to handle Cart CRUD operations
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    permission_classes = [IsBuyer]  # Ensure only authenticated users can access their carts

    def perform_create(self, serializer):
        print(self.request.user)
        
        serializer.save(user_id=self.request.user)
        



class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItems.objects.all()
    serializer_class = CartItemSerializers
    permission_classes = [IsBuyer]  # Ensure only authenticated users can add/update their cart items

    def get_queryset(self):
        cart_id = self.kwargs['cart_id']
        print(cart_id)
        return CartItems.objects.filter(cart_id=cart_id)

    def perform_create(self, serializer):
        cart_id = self.kwargs['cart_id']
        print(cart_id)
        cart = Cart.objects.get(id=cart_id)
        # Automatically associate the cart with the cart item
        serializer.save(cart_id=cart)