from rest_framework import serializers
from .models import User, Consumption

class UserSerializer(serializers.ModelSerializer):
    """
        Serializador del modelo User para modelar y gestionar elementos de esta entidad según los campos especificados. 
    """
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )

class ConsumptionSerializer(serializers.ModelSerializer):
    """
        Serializador del modelo Consumption para modelar y gestionar elementos de esta entidad según los campos especificados. 
    """
    class Meta:
        model = Consumption
        fields = ('id', 'date', 'energy', 'reactive_energy', 'power', 'maximeter', 'reactive_power', 'voltage', 'intensity', 'power_factor')