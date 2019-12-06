from rest_framework import serializers
from .models import Orders, Supplies, Role, OrderDetail, Category #de mi app llamo los modelos

class RoleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Role
        fields = '__all__' #dimensiona todos los campos del modelo 


class SuppliesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Supplies
        fields ='__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'