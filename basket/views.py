from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def view_basket(request):
    """
    Renders the basket contents page
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, pk):
    """
    Add a item and quantify to the shopping basket
    from the product-info page
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if pk in list(basket.keys()):
        basket[pk] += quantity
        messages.success(request, "Item added to basket")

    else:
        basket[pk] = quantity
        messages.success(request, "Item added to basket")

    request.session['basket'] = basket

    return redirect(redirect_url)


def change_quantity(request, pk):
    """
    View to allow users to edit the quantity of
    items in the basket up to a maximum of
    50 bottles of each brand of wine,
    """
    new_quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket')
    redirect_url = request.POST.get('redirect_url')

    if basket[pk] > 50:
        messages.error(request, "You can only buy 50 of the \
            same bottle per order")
    else:
        if new_quantity > 50:
            messages.error(request, "You can only buy 50 of the \
            same bottle per order")
        else:
            basket[pk] = new_quantity
            request.session['basket'] = basket

    return redirect(redirect_url)


def remove_from_basket(request, pk):
    """
    Allows users to remove an item
    from their basket
    """
    basket = request.session.get('basket')
    product = pk
    basket.pop(product)
    request.session['basket'] = basket
    messages.success(request, "Wine from basket")

    return render(request, 'basket/basket.html')
