from django.shortcuts import render

# Create your views here.

def userReviews (request):

    context  = {}
    return render(request, 'reviews/reviews.html', context)
