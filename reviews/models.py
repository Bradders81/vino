from django.db import models
from profiles1 .models import UserProfile
from products .models import Wine


# Create your models here.

class UserReviews(models.Model):
    """
    Table for users add reviews and a sore out of
    5 of teh wines they have bought
    """
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
        
