from .models import (UserProfile,Store,Category,
                     Contact,Address,StoreMenu,
                     Product,Order,CourierProduct,Review)

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class CustomRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name',
                  'date_registered', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
class CustomLoginSerializers(serializers.Serializer):
    username = serializers.CharField
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class StoreListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    class Meta:
        model = Store
        fields = ['id', 'category', 'store_name', 'store_image']

class StoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'category', 'store_name', 'store_image',
                  'created_date','owner','store_image','description']



class CategoryDetailSerializer(serializers.ModelSerializer):
    store_category = StoreListSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name', 'store_category']




class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class StoreMenuListSerializer(serializers.ModelSerializer):
    store = StoreListSerializer(many=True , read_only=True)
    class Meta:
        model = StoreMenu
        fields = ['id', 'menu_name', 'store']


class StoreMenuDetailSerializer(serializers.ModelSerializer):
    menu_store = StoreMenuListSerializer(read_only=True)
    class Meta:
        model = StoreMenu
        fields = ['id', 'menu_name', 'menu_store']


class ProductListSerializer(serializers.ModelSerializer):
    store_menu = StoreMenuListSerializer
    class Meta:
        model = Product
        fields = ['id','product_name','product_image','price']


class ProductDetailSerializer(serializers.ModelSerializer):
    store_product = StoreMenuListSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['id','store_product','product_name','product_image','product_descriptions','price','quantity']



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CourierProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierProduct
        fields = '__all__'



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
