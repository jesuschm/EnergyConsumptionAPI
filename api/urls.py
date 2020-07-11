from django.urls import path
from .views import GetUsers, GetConsumptions, ImportConsumptions, GetEnergyConsumption, GetInstalledPower, GetReactiveEnergyConsumption

urlpatterns = [
    # path('users/', UserList.as_view(), name = 'user_list'),
    # path('consumptions/', ConsumptionList.as_view(), name = 'consumption_list'),
    path('users/', GetUsers.as_view(), name = 'user_list'),
    path('consumptions/', GetConsumptions.as_view(), name = 'consumption_list'),
    path('import-consumptions/', ImportConsumptions.as_view(), name = 'import_consumption'),
    path('energy-consumption/', GetEnergyConsumption.as_view(), name = 'energy_consumption'),
    path('installed-power/', GetInstalledPower.as_view(), name = 'installed_power'),
    path('reactive-energy-consumption/', GetReactiveEnergyConsumption.as_view(), name = 'reactive_energy_consumption'),
]