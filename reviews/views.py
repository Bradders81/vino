from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from profiles1 .models import UserProfile
from .forms import UserReviewForm
from products .models import Wine



# Create your views here.

def user_reviews(request):
    """
    A view to allow users to add a review of the wine
    they have bought
    """

    # user_profile = get_object_or_404(UserProfile, user=request.user)
    # wine_bottle = get_object_or_404(Wine_id, product=request.user)
    form = UserReviewForm

    # if request.method == 'POST':
      
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'review added successfully')

    context  = {'form': form}

    return render(request, 'reviews/reviews.html', context)
