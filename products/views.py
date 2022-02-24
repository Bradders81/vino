from django.shortcuts import render
from django.db.models import Q
from django.contrib import messages
from .models import Wine

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

    context = {'wines': wines}
    return render(request, 'products/products.html', context)


def product_info(request, pk):
    """
    Returns the product selected by the user to the product info page
    """
    wines = Wine.objects.all()
    bottle = Wine.objects.get(id=pk)

    context = {'wines': wines, 'bottle': bottle, }

    return render(request, 'products/product-info.html', context)
