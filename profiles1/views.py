from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.models import User
from checkout.models import Order


@login_required
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
    else:
        form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    context = {
        'user_profile': user_profile,
        'form': form,
        'orders': orders,
    }
    return render(request, 'profiles1/profile.html', context)


@login_required
def delete_user(request, username):
    """
    View to allow a user to delete their account.
    """
    user = User.objects.get(username=username)
    if request.user.is_superuser:
        messages.success(request, 'Not allowedcontact your site Admin')
    else:
        user.delete()
        messages.success(request, f'{user.username} account deleted!')
    return redirect(reverse('home'))


@login_required
def order_history(request, order_number):

    """
    Used to display past orders to the user superusers to make
    sure the site always has at least 1 superuser, superusers cannot
    delete their account
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, ('Past Order confirmation'))

    context = {'order': order, }

    return render(request, 'checkout/checkout_success.html', context)
