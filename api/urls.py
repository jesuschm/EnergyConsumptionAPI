from django.urls import path
from .views import GetUsers, GetConsumptions, ImportConsumptions, GetEnergyConsumption, GetInstalledPower, GetReactiveEnergyConsumption

urlpatterns = [
    # Vista de API para visualizar los usuarios y poder crearlos. Comentado porque se ha securizado con la autenticación para solo acceder por otro endpoint.
    # path('users/', UserList.as_view(), name = 'user_list'), 
    # Vista de API para visualizar los consumos y poder crearlos. Comentado porque se ha securizado con la autenticación para solo acceder por otro endpoint.
    # path('consumptions/', ConsumptionList.as_view(), name = 'consumption_list'), 

    # Endpoint para obtener todos los usuarios del sistema
    path('users/', GetUsers.as_view(), name = 'user_list'),
    # Endpoint para limpiar la base de datos de medida de consumo y volver a poblarla con los elementos de un CSV
    path('import-consumptions/', ImportConsumptions.as_view(), name = 'import_consumption'),
    # Endpoint para obtener todos los consumos del sistema según una fecha de inicio y otra de fin
    path('consumptions/', GetConsumptions.as_view(), name = 'consumption_list'),
    # Endpoint para obtener la energía consumida según una fecha de inicio y otra de fin
    path('energy-consumption/', GetEnergyConsumption.as_view(), name = 'energy_consumption'),
    # Endpoint para obtener la potencia instalada según una fecha de inicio y otra de fin
    path('installed-power/', GetInstalledPower.as_view(), name = 'installed_power'),
    # Endpoint para obtener la energía reactiva consumida según una fecha de inicio y otra de fin
    path('reactive-energy-consumption/', GetReactiveEnergyConsumption.as_view(), name = 'reactive_energy_consumption'),
]