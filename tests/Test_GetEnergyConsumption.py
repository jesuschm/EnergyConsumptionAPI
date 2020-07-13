from django.test import TestCase
from datetime import datetime
from django.http import HttpRequest
from rest_framework.parsers import JSONParser
import requests
import json

from api.models import Consumption
from api.views import getConsumptionAttribute
from EnergyConsumptionAPI.settings import APP_DATETIME_FORMAT


class GetEnergyConsumptionTestCase(TestCase):
    """
       Este test case asegura el buen funcionamiento del cálculo de la energía consumida.               
    """
    def setUp(self):
        """
            El setup consiste en definir un valor por defecto para fecha y cinco para el campo energía (el que será usado para el cálculo).
            Además se fija el valor esperado para la suma de los cinco valores de energía.
            Para terminar el setup, realiza cinco creaciones de la entidad Consumption.
        """
        self.datetime = datetime.now().strftime(APP_DATETIME_FORMAT)
        self.expected_result = 28.5

        energy_values = [5.5, 3.7, 2.8, 5.8, 10.7]  # Sum = 28.5
        for e in energy_values:
            consumption = Consumption(date=self.datetime,
                                            energy=e,
                                            reactive_energy=0.0,
                                            power=0.0,
                                            maximeter=0.0,
                                            reactive_power=0.0,
                                            voltage=0.0,
                                            intensity=0.0,
                                            power_factor=0.0)
            consumption.save()

    def test_getEnergyConsumption(self):
        """
            Para realizar la llamada al método a testear, se utiliza la fecha por defecto para el filtrado y se compara el resultado
            con la suma devuelta por el método.
        """

        filters = {"init_date": self.datetime, "end_date": self.datetime}        
        energySum = getConsumptionAttribute('POST', filters, 'energy', 'sum')        
        self.assertEqual(energySum, self.expected_result)