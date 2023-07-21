from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model 
from .models import Category, Product
from django.contrib.auth import get_user_model 
from.models import ProductImage



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name','category_desc')


class ProductImageSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=ProductImage
        fields=['id','product','image']




       


class ProductSerializer(serializers.ModelSerializer):
    image=ProductImageSerializer(many=True)
    uploaded_images=serializers.ListField(
        child=serializers.ImageField(max_length=10000000,allow_empty_file=False,use_url=False),
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['product_id', 'category_id', 'product_name', 'product_desc','uploaded_images']

UserModel = get_user_model()

from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(max_length=100)
    DOB = serializers.CharField(max_length=80)
    # user_type_data = (
    #     ("1", "vendor"), ("2", "employee")
    #     )
    # user_type = serializers.CharField( choices=user_type_data, max_length=10)
    
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
            DOB=validated_data['DOB'],
            user_type=validated_data['user_type'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password","name","DOB","user_type")

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password','email','name','DOB','user_type', )
        extra_kwargs = {'password': {'write_only': True},'name': {'write_only': True},'DOB':{'write_only': True},'user_type':{'write_only': True}}


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'password', )
        extra_kwargs = {'password': {'write_only': True},'name': {'write_only': True},'user_type':{'write_only': True}}



# class CustomModelSerializer(serializers.Serializer):
    


    





















