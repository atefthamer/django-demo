from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core import serializers
import io
import csv
import os
from django.conf import settings
from .models import AirlineSafety
# Create your views here.


def index(request):
    # return HttpResponse('Index Page')
    if request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile']

        if not uploaded_file.name.endswith('.csv'):
            # handle
            print('-')

        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)

        # read file
        file_data = uploaded_file.read().decode('utf-8')
        io_string = io.StringIO(file_data)
        # next(io_string)
        print(str(file_data))
        # for column in csv.reader(io_string, delemiter=',', qoutechar="|"):
        #     print(column[0])
        filepath = os.path.join(settings.MEDIA_ROOT,  filename)
        print("DIR " + str(filepath), flush=True)
        # airline_safety = AirlineSafety()
        with open(filepath, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            csv_data_iterator = iter(reader)
            next(csv_data_iterator)
            for line in csv_data_iterator:
                print(line[0] + " " + line[1] + " " + line[2] + " " + line[3] + " " +
                      line[4] + " " + line[5] + " " + line[6] + " " + line[7], flush=True)
                airline_safety = AirlineSafety.objects.create(
                    airline=line[0],
                    avail_set_km_per_week=line[1],
                    incidents_85_99=line[2],
                    fatal_accidents_85_99=line[3],
                    fatalities_85_99=line[4],
                    incidents_00_14=line[5],
                    fatal_accidents_00_14=line[6],
                    fatalities_00_14=line[7]
                )
    return render(request, 'index.html')


def airline_safety_data(request):
    # https://dev-yakuza.github.io/en/django/response-model-to-json/
    # safety_data = AirlineSafety.objects.all()
    # safety_data_list = serializers.serialize('json', safety_data)
    # https://stackoverflow.com/questions/12553599/create-json-response-in-django-with-model
    return JsonResponse(list(AirlineSafety.objects.all().values()), safe=False)


def show_airline_safety_data(request):
    safety_data = AirlineSafety.objects.all()
    for data in safety_data:
        print(data.airline, flush=True)
    return render(request, 'data.html', {
        'safety_data': safety_data
    })


def show_visualisations(request):
    return render(request, 'visualisation.html')
