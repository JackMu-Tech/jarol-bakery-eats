# products/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()  # You might want to limit this to featured products
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    """
    View for displaying detailed information about a product.
    """
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def product_create(request):
    """
    View for creating a new product.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    """
    View for updating an existing product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    """
    View for deleting an existing product.
    """
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

@login_required
def category_create(request):
    """
    View for creating a new category.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form': form})

@login_required
def category_update(request, pk):
    """
    View for updating an existing category.
    """
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'products/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    """
    View for deleting an existing category.
    """
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('product_list')
    return render(request, 'products/category_confirm_delete.html', {'category': category})
