from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Table for user details for saving
    delivery information and purchase history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=False, blank=True)
    address_line1 = models.CharField(max_length=80, null=False, blank=True)
    address_line2 = models.CharField(max_length=80, null=True, blank=True)
    city_town = models.CharField(max_length=40, null=False, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwards):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()
