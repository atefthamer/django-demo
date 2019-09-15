from django.db import models

# Create your models here.


class AirlineSafety(models.Model):
    airline = models.CharField(max_length=100)
    avail_set_km_per_week = models.FloatField()
    incidents_85_99 = models.IntegerField()
    fatal_accidents_85_99 = models.IntegerField()
    fatalities_85_99 = models.IntegerField()
    incidents_00_14 = models.IntegerField()
    fatal_accidents_00_14 = models.IntegerField()
    fatalities_00_14 = models.IntegerField()
