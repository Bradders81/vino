from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile


# Create your views here

def profile(request):
    """
    Renders User Profile information
    """
    user_profile = get_object_or_404(Profile, user=request.user)

    context = {'user_profile': user_profile}
    return render(request, 'profiles/profile.html', context)
