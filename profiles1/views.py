from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def profile(request):
    """
    Renders User Profile information
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    context = {
        'user_profile': user_profile,
        'form': form,
        'orders': orders,
    }
    return render(request, 'profiles1/profile.html', context)


def order_history(request, order_number):

    """
    Used to display past orders to the user
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        'Past Order confirmation, order no. {order_number}'
    ))

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)

