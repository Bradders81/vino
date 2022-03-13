from django.shortcuts import render, get_object_or_404
from .models import UserProfile


# Create your views here

def profile(request):
    """
    Renders User Profile information
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {'user_profile': user_profile}
    return render(request, 'profiles1/profile.html', context)
