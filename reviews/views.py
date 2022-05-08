from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserReviewForm
from .models import UserReview
from django.contrib import messages


# Create your views here.
@login_required
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


def product_reviews(request, wine_id):
    """
    A view to display a the reviews for a particular wine
    to a user.  The user does not have to be logged in
    """
    reviews = UserReview.objects.filter(wine_id=wine_id)
    bottle = wine_id
    
    context = {'reviews': reviews, 'bottle': bottle, }

    return render(request, 'reviews/product_reviews.html', context)


def review_details(request, review_id):
    """
    A view to display the full details of a review to a user
    in isolation to the other reviews
    """
    
    bottle = get_object_or_404(UserReview, id=review_id)
    review_id = review_id

    context = {'bottle': bottle, 'review_id': review_id, }

    return render(request, 'reviews/review_details.html', context)


@login_required
def edit_review(request, review_id):
    """
    View to allow a user to edit their review
    """
    review = get_object_or_404(UserReview, id=review_id)
    if request.method == 'POST':
        form = UserReviewForm(request.POST,  instance=review)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated!')
            redirect(reverse('review_details', args=[review.id]))
        else:
            messages.error(request, 'Failed to update review. Please /n'
                                    'ensure the form is valid.')
    else:
        form = UserReviewForm(instance=review)

    context = {'form': form, 'review': review, }

    return render(request, 'reviews/edit_review.html', context)
