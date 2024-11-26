from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from category.models import Category
from category.serializers import CategorySerializers
# Create your views here.
class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers