from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from profiles1 .models import UserProfile
from .forms import UserReviewForm



# Create your views here.

def user_reviews(request,pk):
    """
    A view to allow users to add a review of the wine
    they have bought
    """

    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserReviewForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'review added successfully')

    context  = {}
    return render(request, 'reviews/reviews.html', context)
