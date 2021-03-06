from django.shortcuts import render
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect 
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from statistics import mean
from datetime import datetime
import csv

from .models import User, Consumption
from .serializer import UserSerializer, ConsumptionSerializer
from EnergyConsumptionAPI.settings import APP_DATETIME_FORMAT, INPUT_DATETIME_FORMAT

class JSONResponse(HttpResponse):
    """
    Método de terceros: An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class UserList(generics.ListCreateAPIView):
    """
    Vista de API para visualizar todos los usuarios del sistema 
    """

    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

class ConsumptionList(generics.ListCreateAPIView):
    """
    Vista de API para visualizar todos las medidas de consumo del sistema 
    """

    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    
    queryset = Consumption.objects.all()
    serializer_class = ConsumptionSerializer

class Login(FormView):
    """
        Formulario para logarse visualmente
    """

    # La plantilla html existente en la carpeta /templates/ del proyecto
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('api:user_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, *kwargs)

    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)

        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)

class Logout(APIView):
    """
        Función que destruye el token de identificación del usuario y así realizar el deslogado.
    """

    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    
    def get(self, request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)

class ImportConsumptions(APIView):   
    """
        Función que limpia la base de datos de medidas de consumo y vuelve a poblarla con los elementos de un CSV
    """ 
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def get(self, request, format = None):
        # Primero se limpian todos las medidas existentes
        Consumption.objects.all().delete()

        # Se busca el fichero CSV dentro de la carpeta resources
        with open('./resources/MonitoringReport.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1 # Se obvia la cabecera
                else:
                    # Y si no es cabecera se recogen cada uno de los campos y se construye un objeto Consumption para luego ser grabado en la base de datos
                    dt_date = datetime.strptime(row[0], INPUT_DATETIME_FORMAT)

                    current_consumption = Consumption(date=dt_date.strftime(APP_DATETIME_FORMAT),
                                            energy=row[1],
                                            reactive_energy=row[2],
                                            power=row[3],
                                            maximeter=row[4],
                                            reactive_power=row[5],
                                            voltage=row[6],
                                            intensity=row[7],
                                            power_factor=row[8])

                    current_consumption.save()
                    line_count += 1

        line_count -= 1
        
        # Para terminar, se devuelve al usuario un mensaje informato para saber cuántas lineas se han insertado
        return JSONResponse(f'Lines count: {line_count}')

class GetUsers(APIView):    
    """
        Función que devuelve todos los usuarios del sistema
    """

    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def get(self, request, format = None):
        users = User.objects.all()         
        serializer = UserSerializer(users, many=True)
        
        return JSONResponse(serializer.data)
        
class GetConsumptions(APIView):    
    """
        Función para obtener todos los consumos del sistema según una fecha de inicio y otra de fin
    """

    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def post(self, request, format = None):
        data = JSONParser().parse(request)
        filters = data[0]

        init_date = datetime.now()
        end_date = datetime.now()
        
        if 'init_date' in filters:
            init_date = datetime.strptime(filters['init_date'], APP_DATETIME_FORMAT)
            
        if 'end_date' in filters:
            end_date = datetime.strptime(filters['end_date'], APP_DATETIME_FORMAT)
        
        consumptions = Consumption.objects.filter(date__range=[init_date, end_date]) 
                
        serializer = ConsumptionSerializer(consumptions, many=True)
        return JSONResponse(serializer.data)

class GetEnergyConsumption(APIView):    
    """
        Función para obtener la energía consumida según una fecha de inicio y otra de fin
    """
    
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def post(self, request, format = None):
        data = JSONParser().parse(request)
        # En data[0] se encuentran los filtros
        return JSONResponse(getConsumptionAttribute(request.method, data[0], 'energy', 'sum'))
    
class GetInstalledPower(APIView):
    """
        Función para obtener la potencia instalada según una fecha de inicio y otra de fin
    """
    
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def post(self, request, format = None):
        data = JSONParser().parse(request)
        return JSONResponse(getConsumptionAttribute(request.method, data[0], 'maximeter', 'avg'))

class GetReactiveEnergyConsumption(APIView):
    """
        Función para obtener la energía reactiva consumida según una fecha de inicio y otra de fin
    """

    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def post(self, request, format = None):
        data = JSONParser().parse(request)
        return JSONResponse(getConsumptionAttribute(request.method, data[0], 'reactive_energy', 'sum'))
    
def getConsumptionAttribute(method, filters, attribute, function, consumptionSet = Consumption):
    """
        Método que permite realizar un cálculo sobre un campo de la entidad Consumption. 
    """

    if method == 'POST':
        
        init_date = datetime.now()
        end_date = datetime.now()
        
        if 'init_date' in filters:
            init_date = datetime.strptime(filters['init_date'], APP_DATETIME_FORMAT)
            
        if 'end_date' in filters:
            end_date = datetime.strptime(filters['end_date'], APP_DATETIME_FORMAT)
        
        consumptions = consumptionSet.objects.filter(date__range=[init_date, end_date])
    else:
        return HttpResponse(status=403)
    
    if function == 'sum':
        energyConsumption= sum([ getattr(c, attribute) for c in consumptions.all() ])
    elif function == 'avg':
        energyConsumption= mean([ getattr(c, attribute) for c in consumptions.all() ])       
    
    return energyConsumption