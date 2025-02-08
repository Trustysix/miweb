from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'date')
    search_fields = ('name',)
    list_filter = ('date',)

admin.site.register(Product, ProductAdmin)