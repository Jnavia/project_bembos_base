from rest_framework import viewsets
from .models import Role, Orders, Supplies, OrderDetail
from .serializers import RoleSerializer, OrdersSerializer, SuppliesSerializer, OrderDetailSerializer

# Create your views here.

class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly] #con esto desaparece el formulario


class OrdersView(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class SuppliesView(viewsets.ModelViewSet):
    queryset = Supplies.objects.all()
    serializer_class = SuppliesSerializer


class OrderDetailView(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer