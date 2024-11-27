from rest_framework import serializers
from .models import Product
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =['name','description','price','quantity_in_stock','category_id','image','status']




   
    
    
   
   
    
