from django.shortcuts import render
from product.models import Product
from product.serializers import ProductSerializers
from account.permission import IsSeller
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import viewsets
from vendor.models import Vendor
# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser,FormParser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsSeller]

    def perform_create(self,serializer):
        print(serializer)
        vendor  = Vendor.objects.get(user_id=self.request.user.id)
        print(vendor.id)
        serializer.save(vendor_id=vendor)
