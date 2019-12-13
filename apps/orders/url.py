from django.urls import path
from .viewsets import CategoryViewSet,SupplyViewSet,Order_StateViewSet,OrderDetailViewSet,OrderViewSet,UserViewSet,GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'category',CategoryViewSet)
router.register(r'supply',SupplyViewSet,base_name='Supply')
router.register(r'order_state',Order_StateViewSet)
router.register(r'order',OrderViewSet)
router.register(r'orderdetail',OrderDetailViewSet)
router.register(r'user',UserViewSet)
router.register(r'group',GroupViewSet)

urlpatterns =router.urls
