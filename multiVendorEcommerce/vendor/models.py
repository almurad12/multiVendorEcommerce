from django.db import models
from account.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Vendor(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    vendor_name = models.CharField(max_length=30)
    contact_number = PhoneNumberField(unique=True, blank=True, null=True)
    store_name = models.CharField(max_length=30)
    store_logo = models.ImageField(upload_to='storelogo/')
    store_description = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name