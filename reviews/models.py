from django.db import models
from django.contrib.auth.models import User
from products .models import Wine

# Create your models here.
class UserReview(models.Model):
    """
    Model for users add reviews and a sore out of
    5 of the wines they have bought
    """
    SCORES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (4, '5'),
    )

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    review_name = models.CharField(max_length=50, null=True, blank=True)
    wine = models.ForeignKey(
        Wine, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        choices=SCORES, null=False, blank=True, default=1)
    review = models.TextField(null=True, blank=True)
    buy_again = models.BooleanField(default=True)

    def __str__(self):
        return self.wine.wine_name

