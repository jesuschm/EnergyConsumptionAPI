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
    def setUp(self):
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

        filters = {"init_date": self.datetime, "end_date": self.datetime}        
        energySum = getConsumptionAttribute('POST', filters, 'energy', 'sum')        
        self.assertEqual(energySum, self.expected_result)