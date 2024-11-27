from vendor.models import Vendor
from rest_framework import serializers

class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields =['vendor_name','contact_number','store_name','store_logo','store_description']
        
        
