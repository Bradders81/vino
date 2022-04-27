from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from profiles1 .models import UserProfile
from products .models import Wine
from django.db.models import Sum


# Create your models here.



class UserReview(models.Model):
    """
    Table for users add reviews and a sore out of
    5 of teh wines they have bought
    """
    SCORES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (4, '5'),
    )

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    review_name = models.CharField(max_length=50, null=True, blank=True)
    wine = models.ForeignKey(
        Wine, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(
        choices=SCORES, null=False, blank=False, default=1)
    review = models.TextField(null=True, blank=True)
    buy_again = models.BooleanField(default=True)

    def __str__(self):
        return self.wine

