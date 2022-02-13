from django.db import models

import uuid


# Create your models here.



class Wine(models.Model):
    """
    Model of the wines in the database
    """
    class Meta:
        verbose_name_plural = 'Wine'

    Red = 'Red'
    White = 'White'
    Rosé = 'Rosé'

    WINE_TYPES = [
        (Red, Red),
        (White, White),
        (Rosé, Rosé),
    ]

    wine_name = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    country = models.CharField(max_length=50, null=True, blank=True)
    winery = models.CharField(max_length=50, null=True, blank=True)
    # rating = models.ManyToManyField(Reviews, models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    wine_type = models.CharField(choices=WINE_TYPES, max_length=5)
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.wine_name

