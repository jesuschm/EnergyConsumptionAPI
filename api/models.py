from django.db import models

class User(models.Model):
    """
        Este modelo define el concepto de usuario. 

        Campos: id, clave primaria auto incremental
                username, nombre de usuario con el que se le identifica

        TODO: añadir más campos de información personal
    """

    id = models.AutoField(primary_key = True)
    username = models.CharField('username', max_length= 255)

    def __str__(self):
        return '{0}'.format(self.username)

class Consumption(models.Model):
    """
        Este modelo define el concepto de medida de consumo.

        Campos: id, clave primera auto incremental
                date, fecha de la medición
                energy, medida de energía consumida por hora (kWh)
                reactive_energy, energía reactiva medida (kVArh)
                power, potencia consumida (kW)
                maximeter, potencia máxima disponible medida por el maximetro (kW)
                reactive_power, potencia reactiva medida (kVAr)
                voltage, tensión medida (V)
                intentisity, intensidad medida (A)
                power_factor, factor de potencia de la medida (φ)
    """
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