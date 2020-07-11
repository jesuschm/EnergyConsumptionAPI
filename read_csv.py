from dashboardapp.models import Consumption
from dashboardapp.serializers import ConsumptionSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from datetime import datetime
import csv

with open('resources/MonitoringReportLittle.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            dt_date = datetime.strptime(row[0], '%d %b %Y %H:%M:%S')
            
            #print(f'\tDate {fdate}, Energy: {row[1]}, and Power {row[3]}.')
                
            current_consumption = Consumption(date = dt_date.strftime("%Y-%m-%d %H:%M:%S"), 
                                    energy = row[1],
                                    reactive_energy = row[2],
                                    power = row[3],
                                    maximeter = row[4],
                                    reactive_power = row[5],
                                    voltage = row[6],
                                    intensity = row[7],
                                    power_factor = row[8])
            
            current_consumption.save()
            line_count += 1


serializer = ConsumptionSerializer(current_consumption)

content = JSONRenderer().render(serializer.data)

