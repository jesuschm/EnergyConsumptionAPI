from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField('username', max_length= 255)

    def __str__(self):
        return '{0}'.format(self.username)

class Consumption(models.Model):
    id = models.AutoField(primary_key = True)
    date = models.DateTimeField()
    energy = models.FloatField(default=0.0)
    reactive_energy = models.FloatField(default=0.0)
    power = models.FloatField(default=0.0)
    maximeter = models.FloatField(default=0.0)
    reactive_power = models.FloatField(default=0.0)
    voltage = models.FloatField(default=0.0)
    intensity = models.FloatField(default=0.0)
    power_factor = models.FloatField(default=0.0)

    def __str__(self):
        return '{0},{1},{2},{3}'.format(self.date, self.energy,self.reactive_energy,self.maximeter)