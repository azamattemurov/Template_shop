from django.contrib import admin

from orders.models import OrderModel, OrderItem
from orders.forms import OrderModelForm


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at', 'updated_at']



@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product_name','size','price','quantity']
    search_fields = ['product_name']


