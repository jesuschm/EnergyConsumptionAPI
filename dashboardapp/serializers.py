from rest_framework import serializers
from .models import Consumption

class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = ('id', 'date', 'energy', 'reactive_energy', 'power', 'maximeter', 'reactive_power', 'voltage', 'intensity', 'power_factor')