from django.db import models

# Create your models here.
class Consumption(models.Model):

    date = models.DateTimeField()
    energy = models.FloatField(default=0.0)
    reactive_energy = models.FloatField(default=0.0)
    power = models.FloatField(default=0.0)
    maximeter = models.FloatField(default=0.0)
    reactive_power = models.FloatField(default=0.0)
    voltage = models.FloatField(default=0.0)
    intensity = models.FloatField(default=0.0)
    power_factor = models.FloatField(default=0.0)