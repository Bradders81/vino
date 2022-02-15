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

    if request.GET.get('category'):
        category = request.GET.get('category')
        wines = wines.filter(wine_type=category)
        
        if request.GET.get('search_query'):
            search_query = request.GET.get('search_query')
            wines = Wine.objects.filter(
                Q(wine_name__icontains=search_query) |
                Q(wine_type__icontains=search_query) |
                Q(country__icontains=search_query) |
                Q(year__icontains=search_query))

            if not wines:
                messages.error(request, "Nothing matches your search")

    context = {'wines': wines}
    return render(request, 'products/products.html', context)


def sorting_products(request):
    """
    Allows users to sort prodcuts by diffrent catagories
    assending and desending on the products page.
    """
    sort = None
    wines = wine.objects.get.all()

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = wines.annotate(lower_name=Lower('name'))
        if 'direction' in request.GET:
            if direction =='desc':
                sortkey = f'-{sortkey}'

    current_sorting = f'{sort}_{direction}'

    context = {'current_sorting': current_sorting}
    return render(request, 'products/products.html', context)


def product_info(request, pk):
    """
    Returns the product selected by the user to the product info page
    """
    wines = Wine.objects.all()
    bottle = Wine.objects.get(id=pk)

    context = {'wines': wines, 'bottle': bottle, }

    return render(request, 'products/product-info.html', context)

