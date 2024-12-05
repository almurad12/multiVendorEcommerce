from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from status.models import Status
from status.serializers import serializers ,StatusSerializers
# Create your views here.
class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Status.objects.all()
    serializer_class = StatusSerializers