from rest_framework import serializers
from .models import User, Consumption

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )

class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = ('id', 'date', 'energy', 'reactive_energy', 'power', 'maximeter', 'reactive_power', 'voltage', 'intensity', 'power_factor')