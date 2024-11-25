from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from .models import CustomUser
# from .models import Product, Order  # Assuming you have models for Product and Order.

class IsSeller(BasePermission):
    """
    Allows access only to sellers (users with 'seller' role).
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the 'seller' role.
        return request.user.is_authenticated and request.user.is_seller == 'True'
    

class IsBuyer(BasePermission):
    """
    Allows access only to sellers (users with 'seller' role).
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and has the 'Buyer' role.
        return request.user.is_authenticated and request.user.is_buyer == 'True'