from django.urls import path, include
from .viewsets import RoleView, OrdersView, SuppliesView, OrderDetailView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('role', RoleView)
router.register('orders', OrdersView)
router.register('supplies', SuppliesView) #asi está en la ruta
router.register('orders_detail', OrderDetailView) #asi está en la ruta

# urlpatterns = [
#     path('bembos/', include(router.urls))
# ]

urlpatterns =router.urls