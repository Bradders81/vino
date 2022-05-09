from django.db import models
from django.contrib.auth.models import User
from products .models import Wine


# Create your models here.
class UserReview(models.Model):
    """
    Model for users add reviews and a sore out of
    5 of the wines they have bought
    """

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    review_name = models.CharField(
        max_length=50, null=False, blank=False, default='No Title')
    wine = models.ForeignKey(
        Wine, on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(null=True, blank=True)
    buy_again = models.BooleanField(default=True)

    def __str__(self):
        return self.wine.wine_name
