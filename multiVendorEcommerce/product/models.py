from django.db import models
from vendor.models import Vendor
from category.models import Category
# Create your models here.

class Product(models.Model):
    vendor_id = models.ForeignKey(Vendor,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimg/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)