from django.contrib import admin

from .models import Product, Customer, Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['placed_at', 'status', 'customer']
    inlines = [OrderItemInline]  # This will allow you to add/edit OrderItems from within the Order admin page.
    list_filter = ['status', 'placed_at']
    search_fields = ['customer__first_name', 'customer__last_name']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity']
    search_fields = ['product__name', 'order__id']
