from django.shortcuts import render

# Create your views here.

def user_reviews(request,):
    """
    A view to allow users to add a review of the wine
    they have bought
    """

    # user_profile = get_object_or_404(UserProfile, user=request.user)
    # if request.method == 'POST':
    #     form = UserReviewForm(request.POST, instance=user_profile)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'review added successfully')

    context  = {}
    return render(request, 'reviews/reviews.html', context)
