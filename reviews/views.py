from django.shortcuts import render

# Create your views here.

def userReviews (request,):
    """
    A view to allow users to add a review of the wine
    they have bought
    """

    context  = {}
    return render(request, 'reviews/reviews.html', context)
