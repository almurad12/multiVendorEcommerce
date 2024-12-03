from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from .models import CustomUser
class SellerRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
       model = CustomUser
       fields = ['first_name','last_name','email','password','password2']

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match"})
        return attrs
    def create(self, validated_data):
          user = CustomUser.objects.create_user(
            email= validated_data['email'],
            password= validated_data['password'],
            # first_name = validated_data['first_name'],
            # last_name = validated_data['last_name'],
            is_seller = True,
            is_staff = True,
            is_active = True
            
          )
          return user
        #   validated_data['is_seller'] = Truecls
        #   validated_data['is_staff'] = True
        #   validated_data['is_active'] = True
        #   super().create(validated_data)
        #   return Response({"response":"user created successfully"})

    
            # return user.
  

class BuyerRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
       model = CustomUser
       fields = ['first_name','last_name','email','password','password2']

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match"})
        return attrs
    def create(self, validated_data):
          user = CustomUser.objects.create_user(
            email= validated_data['email'],
            password= validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            is_staff = True,
            is_buyer = True,
            is_active = True
            
          )
          return user
    
