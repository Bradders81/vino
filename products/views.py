from django.shortcuts import render
from .models import Wine
# Create your views here.


def products(request):
    """
    Returns the Prodcuts  page
    """
    wines = Wine.objects.all()
    
    context = {
        'wines': wines,
    }
    return render(request, 'products/products.html', context)


def product_info(request, pk):
    """
    Returns the product selected by the user to the product info page
    """
    wines = Wine.objects.all()
    bottle = Wine.objects.get(id=pk)

    context = {
        'wines': wines,
        'bottle': bottle,
    }

    return render(request, 'products/product-info.html', context)

