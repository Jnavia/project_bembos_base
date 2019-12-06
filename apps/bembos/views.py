from django.shortcuts import render
from rest_framework import generics
from .models import Role, Orders, Supplies, OrderDetail
from .serializers import RoleSerializer, OrdersSerializer, SuppliesSerializer, OrderDetailSerializer

# Create your views here.