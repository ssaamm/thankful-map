from django.db import models
from geoposition.fields import GeopositionField

class Thing(models.Model):
    description = models.CharField(max_length=160)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)

    def __str__(self):
        return self.description
