from django.db import models
import uuid


# Create your models here.


class Wine(models.Model):
    """
    Model of the wine in the database
    """
    class Meta:
        verbose_name_plural = 'Wine'

    name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, default="placeholder.png")
    country = models.CharField(max_length=50, null=True, blank=True)
    winery = models.CharField(max_length=50, null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
