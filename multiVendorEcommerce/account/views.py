from django.shortcuts import render
from .serializers import SellerRegistrationSerializer,BuyerRegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import CustomUser
# Create your views here.
@api_view(['post'])
def Sellerregister(request):
    if request.method == 'POST':
        # data = request.data
        print(request.data)
        serializer = SellerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            user = serializer.save()

            return Response({
                # "user": SellerRegistrationSerializer(user),
                "message": "Seller Account Created Successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['post'])
def buyerregister(request):
    if request.method == 'POST':
        serializer = BuyerRegistrationSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message":"Buyer Acccount Created Successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




