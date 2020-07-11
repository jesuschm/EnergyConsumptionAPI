from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from dashboardapp.models import Consumption
from dashboardapp.serializers import ConsumptionSerializer
from datetime import datetime
from reportapp.settings import APP_DATETIME_FORMAT, INPUT_DATETIME_FORMAT
import csv

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def readCsv(request):
    Consumption.objects.all().delete()

    with open('./resources/MonitoringReportLittle.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
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
    return JSONResponse(f'Lines count: {line_count}')

@csrf_exempt
def getConsumptionHistory(request):
    
    if request.method == 'GET':
        consumptions = Consumption.objects.all()

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        filters = data[0]

        init_date = datetime.now()
        end_date = datetime.now()
        
        if 'init_date' in filters:
            init_date = datetime.strptime(filters['init_date'], APP_DATETIME_FORMAT)
            
        if 'end_date' in filters:
            end_date = datetime.strptime(filters['end_date'], APP_DATETIME_FORMAT)
        
        consumptions = Consumption.objects.filter(date__range=[init_date, end_date]) 
    else:
        return HttpResponse(status=400)
            
    serializer = ConsumptionSerializer(consumptions, many=True)
    return JSONResponse(serializer.data)

@csrf_exempt
def getEnergyConsumption(request):
    return getConsumptionAttribute(request, 'energy', 'sum')

@csrf_exempt
def getInstalledPower(request):
    return getConsumptionAttribute(request, 'maximeter', 'avg')

@csrf_exempt
def getReactiveEnergyConsumption(request):
    return getConsumptionAttribute(request, 'reactive_energy', 'sum')

def getConsumptionAttribute(request, attribute, function):

    if request.method == 'GET':
        consumptions = Consumption.objects.all()        
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        filters = data[0]

        init_date = datetime.now()
        end_date = datetime.now()
        
        if 'init_date' in filters:
            init_date = datetime.strptime(filters['init_date'], APP_DATETIME_FORMAT)
            
        if 'end_date' in filters:
            end_date = datetime.strptime(filters['end_date'], APP_DATETIME_FORMAT)
        
        consumptions = Consumption.objects.filter(date__range=[init_date, end_date])
    else:
        return HttpResponse(status=400)
    
    if function == 'sum':
        energyConsumption= sum([ getattr(c, attribute) for c in consumptions.all() ])
    elif function == 'avg':
        energyConsumption= mean([ getattr(c, attribute) for c in consumptions.all() ])       
    
    return JSONResponse(energyConsumption)