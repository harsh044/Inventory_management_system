from django.contrib import admin
from .models import Inventory
# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price','product_category') 
    search_fields = ('product_name',)                   

admin.site.register(Inventory, InventoryAdmin)