from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from profiles1 .models import UserProfile
from products .models import Wine
from django.db.models import Sum


# Create your models here.

class Meta:
    verbose_name_plural = 'UserReviews'

class UserReviews(models.Model):
    """
    Table for users add reviews and a sore out of
    5 of teh wines they have bought
    """

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    review_name = models.CharField(max_length=50, null=True, blank=True)
    wine_name = models.ManyToManyField(Wine)
    date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=False, blank=False, default=1)
    review = models.TextField(max_length=300, null=True, blank=True)
    buy_again = models.BooleanField(default=True)

