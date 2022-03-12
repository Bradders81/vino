from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.contrib import messages
import stripe
import json
from basket.contexts import basket_contents
from products.models import Wine
from .forms import OrderForm
from .models import Order, OrderLineItem

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket':json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be made \
            right now. Please try again later.')
        return HttpResponse(content=e, status=400)



def checkout(request):
    """
    Handles checkout logic and stripe
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode':  request.POST['postcode'],
            'city_town': request.POST['city_town'],
            'address_line1': request.POST['address_line1'],
            'address_line2': request.POST['address_line2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Wine.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )

                    order_line_item.save()
                except Wine.DoesNotExist:
                    messages.error(request, (
                        "Your basket and our database do not match."
                        "Please contact us for assistance.")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))
        
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Order error. Please try again')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "Your bag is empty")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        
     }

    return render(request, 'checkout/checkout.html', context,)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    

    if 'basket' in request.session:
        del request.session['basket']
    
    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
