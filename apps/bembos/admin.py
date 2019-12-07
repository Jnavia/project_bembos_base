from django.contrib import admin
from .models import Role, Orders, Supplies, OrderDetail, Category
 
# Register your models here.
admin.site.register(Role)
admin.site.register(Orders)
admin.site.register(Supplies)
admin.site.register(OrderDetail)
admin.site.register(Category)
