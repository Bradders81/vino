from django.contrib.auth.models import User
import uuid
from django.db import models

class Profile(models.Model):
    """
    Table for user details
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    city_town = models.CharField(max_length=50, blank=True, null=True)
    postcode = models.CharField(max_length=50, blank=True, null=True)
    # review = models.ForeignKey(
    #     Reviews, on_delete=models.SET_NULL, null=True, blank=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.user.username
