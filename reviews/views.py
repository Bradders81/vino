from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserReviewForm
from .models import UserReview

# from products .models import Wine


# Create your views here.
def user_reviews(request):
    """
    A view to allow users to add a review of the wine
    they have bought
    """
    form = UserReviewForm

    if request.POST:
        form = UserReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(
                request, ("Your review has been added."))
        return redirect('reviews')

    context = {'form': form}

    return render(request, 'reviews/reviews.html', context)


