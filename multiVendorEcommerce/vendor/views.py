from django.shortcuts import render
from vendor.models import Vendor
from vendor.serializers import VendorSerializers
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.parsers import MultiPartParser, FormParser
from account.permission import IsSeller
from rest_framework import viewsets
# Create your views here.
class vendorViewset(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializers
    # permission_classes = [IsAuthenticated,IsSeller,IsAdminUser]
    permission_classes = [IsSeller]

    def perform_create(self,serializer):
        serializer.save(user_id =self.request.user)


