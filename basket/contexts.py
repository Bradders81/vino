from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Wine


def basket_contents(request):
    """
    Handles the basket total on the basket page
    """
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        wine = get_object_or_404(Wine, pk=item_id)
        total += quantity * wine.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'wine': wine,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count
    }

    return context