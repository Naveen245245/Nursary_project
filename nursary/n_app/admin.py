from django.contrib import admin

# Register your models here.
from .models import Owner, Nursary, Farmer, Product, Order, Bed


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'dp']


admin.site.register(Owner, OwnerAdmin)


class NursaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'owner', 'rows', 'columns']


admin.site.register(Nursary, NursaryAdmin)


class FarmerAdmin(admin.ModelAdmin):
    list_display = ['name', 'adhar_num',
                    'phone_num', 'land_survey_num', 'address']


admin.site.register(Farmer, FarmerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price']


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'farmer_c',
                    'nursary_p', 'qty', 'amount', 'bed']


admin.site.register(Order,OrderAdmin)


class BedAdmin(admin.ModelAdmin):
    list_display = ['id', 'capacity', 'status', 'nursary']


admin.site.register(Bed, BedAdmin)
