from django.contrib import admin
from . import models

# Register your models here.
class StockModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category', "get_status", "last_updated"]

    def get_status(self, obj):
        """
        Get the status of the product in stock
        """
        if obj.quantity <= 0:
            return "out of stock"
        return "in stock"

admin.site.register(models.Stock, StockModelAdmin)