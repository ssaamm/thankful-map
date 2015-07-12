from django.db import models
from geoposition.fields import GeopositionField

class Thing(models.Model):
    description = models.CharField(max_length=160)
    location = GeopositionField()
