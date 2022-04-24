from django.shortcuts import render, redirect
from products.models import Wine

# Create your views here.


def view_basket(request):
    """
    Renders the basket contents page
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, pk):

    """
    Add a item and quantify to the shopping basket
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if pk in list(basket.keys()):
        basket[pk] += quantity
       

    else:
        basket[pk] = quantity

    request.session['basket'] = basket
    
    return redirect(redirect_url)


