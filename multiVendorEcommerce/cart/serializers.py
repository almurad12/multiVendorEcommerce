from rest_framework import serializers
from cart.models import CartItems,Cart
class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields =['id','cart_id','product_id','quantity','created_at', 'updated_at',]
        read_only_fields = ['user_id']

class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializers(many=True,read_only = True)
    class Meta:
        model = Cart
        fields =['id','user_id','created_at', 'updated_at', 'items']
        read_only_fields = ['user_id']