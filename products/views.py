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
