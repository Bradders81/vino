from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Wine
from .forms import ProductForm

# Create your views here.

def products(request):
    """
    Returns the Prodcuts page and handles
    search queries for products
    """
    wines = Wine.objects.all()

    # Handles search queries
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        wines = Wine.objects.filter(
            Q(wine_name__icontains=search_query) |
            Q(wine_type__icontains=search_query) |
            Q(country__icontains=search_query) |
            Q(year__icontains=search_query))
        
        if not wines:
            messages.error(request, "Nothing matches your search")

    # Handles filter btn's (All Wines, Reds, Whites, Rose)
    if request.GET.get('wine_type'):
        wine_type = request.GET.get('wine_type')
        wines = wines.filter(wine_type=wine_type)

        if not wines:
            messages.error(request, "Nothing matches your search")

    context = {'wines': wines}
    return render(request, 'products/products.html', context)

def product_info(request, pk):
    """
    Returns the product selected by the user to the product info page
    """
    wines = Wine.objects.all()
    bottle = get_object_or_404(Wine, id=pk)

    context = {'wines': wines, 'bottle': bottle, }

    return render(request, 'products/product-info.html', context)


@login_required
def add_product(request):
    """
    View for adding products to the online shop
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Added')
        else:
            messages.error(
                request, 'Products not added, Please check form is valid')
    else:
        form = ProductForm
    context = {'form': form, }

    return render(request, 'products/add_product.html', context)

@login_required
def edit_product(request, pk):
    """
    View to allow editing a product in the online shop
    """
    product = get_object_or_404(Wine, id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product-info', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
   

    context = {'form': form, 'product': product, }
    
    return render(request, 'products/edit_product.html', context)

@login_required
def delete_product(request, pk):
    """ Delete a  wine product from the online shop """
    product = get_object_or_404(Wine, id=pk)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
