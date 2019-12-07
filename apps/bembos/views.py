from django.shortcuts import render
from rest_framework import generics
from .models import Role, Orders, Supplies, OrderDetail, Category
from .serializers import RoleSerializer, OrdersSerializer, SuppliesSerializer, OrderDetailSerializer, CategorySerializer

# Create your views here.