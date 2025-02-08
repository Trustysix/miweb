from django.shortcuts import render, redirect
from .models import Product, InventoryRecord
from .forms import ProductForm, InventoryRecordForm

def index(request):
    products = Product.objects.all()
    inventory_records = InventoryRecord.objects.all()
    return render(request, 'products/index.html', {'products': products, 'inventory_records': inventory_records})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'products/add_product.html', {'form': form})

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        product.quantity = quantity
        product.save()
        return redirect('index')

    return render(request, 'products/edit_product.html', {'product': product})

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('index')