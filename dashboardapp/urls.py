from django.conf.urls import url
from dashboardapp import views

urlpatterns = [
    url('admin/readCsv', views.readCsv),
    url('dashboard', views.getConsumptionHistory),   
    url('consumption/consumed-energy', views.getEnergyConsumption), 
    url('consumption/reactive-energy', views.getReactiveEnergyConsumption), 
    url('consumption/installed-power', views.getInstalledPower), 
]