from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

class OrderAdmin(admin.ModelAdmin):
    """
    Sets the order the fields and which are readonly
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total',)

    fields = ('order_number', 'user_profile', 'date', 'name', 'email',
              'phone_number', 'address_line1', 'address_line2', 'city_town',
              'postcode', 'order_total',)

    list_display = ('order_number', 'date', 'name',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)

