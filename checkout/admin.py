from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdmin,)
    readonly_fields = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'street_address1',
        'street_address2',
        'town_or_city',
        'postcode',
        'country',
        'date',
    )

    fields = (
        'order_number', 
        'date', 
        'full_name', 
        'email', 
        'phone_number', 
        'postcode', 
        'town_or_city', 
        'street_address1', 
        'street_address2', 
        'country', 
        'delivery_cost', 
        'order_total', 
        'grand_total',
    )

    list_display = (
        'order_number', 
        'date', 
        'full_name', 
        'delivery_cost', 
        'order_total', 
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
