from django.contrib import admin
from .models import CustomUser
from category.models import Category
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
