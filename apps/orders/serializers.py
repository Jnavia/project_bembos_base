from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Category,Supply,Order_State,Order,OrderDetail


class UserSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']   

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']     

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Category
       fields = ['id', 'name', 'url']

class SupplySerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Supply
        fields = ['id', 'name', 'image', 'price', 'created_at', 'status', 'category']

class Order_StateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Order_State
       fields = ['id', 'name', 'url']

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = [            
            'order',
            'supply',
            'combo',
            'quantity'
        ]
        read_only_fields = ('id',)
        depth=2

class OrderSerializer(serializers.ModelSerializer):
    orderdetails=OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id',            
            'description',
            'customer',
            'status',
            'orderdetails'
        ]
        
    
    def create(self, validate_data):
        orderdetails = validate_data.pop('orderdetails')
        order =  Order.objects.create(**validate_data)
        for orderdetail in orderdetails:
            orderdetail.objects.create(**orderdetail, order=order)
        return order
   






    

    