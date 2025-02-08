from django import forms
from .models import Product, InventoryRecord

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'quantity']

class InventoryRecordForm(forms.ModelForm):
    class Meta:
        model = InventoryRecord
        fields = ['product', 'quantity']