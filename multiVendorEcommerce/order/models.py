from django.db import models
from account.models import CustomUser
from status.models import Status
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    order_status = models.ForeignKey(Status, related_name='orders', on_delete=models.SET_NULL, null=True)
    order_date = models.DateField()
    shipping_address = models.CharField(max_length=255)
    total_amount = models.IntegerField()
    payment_status = models.ForeignKey(Status, related_name='payment_status', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
            return f"Order {self.order_id} - {self.user.email}"