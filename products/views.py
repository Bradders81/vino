from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib import messages
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


def add_product(request):
    """
    View for adding products to the online shop
    """
    if request.method == 'POST':
        form = ProductForm(request.Post, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Added')
        else:
            messages.error(
                request, 'Products not added, Please check form is valid')
    else:
        form = ProductForm
    context = {'form': form, }

    return render(request, 'products/add-product.html', context)

    
