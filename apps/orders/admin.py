from django.contrib import admin
from .models import Supply,Category,Order_State,Order,OrderDetail

# Register your models here.
admin.site.register(Supply)
admin.site.register(Category)
admin.site.register(Order_State)
admin.site.register(Order)
admin.site.register(OrderDetail)
