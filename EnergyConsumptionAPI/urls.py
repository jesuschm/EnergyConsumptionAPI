"""EnergyConsumptionAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from api.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),

    # Parte de la ruta para los métodos de la api (versión 1)
    path('api/v1/', include(('api.urls', 'api'))),
    # Endpoint para obtener el token del usuario según unas credenciales. 
    path('generate_token/', views.obtain_auth_token),
    # Interfaz de prueba para logarse visualmente y no mediante el endpoint de generate_token
    path('login/', Login.as_view(), name = 'Login'),
    # Endpoint para destruir el token de identificación del usuario y así deslogarse.
    path('logout/', Logout.as_view(), name = 'Logout'),
]
