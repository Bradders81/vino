from django.shortcuts import render, redirect
from .forms import UserReviewForm
from .models import UserReview
from django.contrib import messages


# Create your views here.
def user_reviews(request):
    """
    A view to allow users to add a review of the wine
    they have bought.  Only login in users can leave
    a review
    """
    form = UserReviewForm
    reviews = UserReview.objects.filter(user=request.user)

    if request.POST:
        form = UserReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(
                request, ("Your review has been added."))
        return redirect('reviews')
    
    context = {'form': form, 'reviews': reviews, }

    return render(request, 'reviews/reviews.html', context)


def display_wine_reviews(request, wine_id):
    """
    A view to display a the reviews for a particular wine
    to a user.  The user does not have to be logged in
    """
    reviews = UserReview.objects.filter(wine_id=wine_id)
    bottle = wine_id
    
    
    context = {'reviews': reviews, 'bottle': bottle, }

    return render(request, 'reviews/product_reviews.html', context)

