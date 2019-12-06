from django.urls import path, include
from .viewsets import RoleView, OrdersView, SuppliesView, OrderDetailView, CategoryView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('role', RoleView)
router.register('orders', OrdersView)
router.register('supplies', SuppliesView)
router.register('orders_detail', OrderDetailView)
router.register('category', CategoryView,)

# urlpatterns = [
#     path('bembos/', include(router.urls))
# ]

urlpatterns =router.urls