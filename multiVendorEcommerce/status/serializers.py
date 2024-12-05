from rest_framework import serializers
from status.models import Status
class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['name']
