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
    from the product-info page
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if pk in list(basket.keys()):
        basket[pk] += quantity
       

    else:
        basket[pk] = quantity

    request.session['basket'] = basket
    # This cookie is needed for the change quantity view below
    request.session['quantity'] = quantity

    return redirect(redirect_url)


def change_quantity(request, pk):
    """
    View to allow users to edit the quantity of
    items in the basket, up to a maximum of 50 per item
    """
    new_quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket')
    current_quantity = request.session.get('quantity')

    if new_quantity > current_quantity:
        updated_quantity = int(new_quantity - current_quantity)

        if updated_quantity + current_quantity <= 50:
            basket[pk] += updated_quantity
        else:
            updated_quantity = 50
            basket[pk] += updated_quantity
    else:
        updated_quantity = int(current_quantity - new_quantity)
        basket[pk] -= updated_quantity

    request.session['basket'] = basket
    request.session['quantity'] = new_quantity

    return redirect(redirect_url)

