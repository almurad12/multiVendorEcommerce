from django.contrib import admin
from .models import CustomUser
from category.models import Category
from product.models import Product
from vendor.models import Vendor
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Vendor)