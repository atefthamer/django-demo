from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.core import serializers
import io
import csv
import os
from django.conf import settings
from .models import AirlineSafety
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
# Create your views here.


def index(request):
    # return HttpResponse('Index Page')
    if request.method == 'POST' and request.FILES['myfile']:
        uploaded_file = request.FILES['myfile']

        if not uploaded_file.name.endswith('.csv'):
            return render(request, 'index.html')

        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)

        # read file
        file_data = uploaded_file.read().decode('utf-8')
        io_string = io.StringIO(file_data)

        filepath = os.path.join(settings.MEDIA_ROOT,  filename)
        # print("DIR " + str(filepath), flush=True)
        # Open file and store inside database table
        # Note: input can already be inside the table
        with open(filepath, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            csv_data_iterator = iter(reader)
            next(csv_data_iterator)
            for line in csv_data_iterator:
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


class AirlineCreate(CreateView):
    model = AirlineSafety
    fields = [
        'airline',
        'avail_set_km_per_week',
        'incidents_85_99',
        'fatal_accidents_85_99',
        'fatalities_85_99',
        'incidents_00_14',
        'fatal_accidents_00_14',
        'fatalities_00_14'
    ]


class AirlineForm(ModelForm):
    class Meta:
        model = AirlineSafety
        fields = [
            'airline',
            'avail_set_km_per_week',
            'incidents_85_99',
            'fatal_accidents_85_99',
            'fatalities_85_99',
            'incidents_00_14',
            'fatal_accidents_00_14',
            'fatalities_00_14'
        ]


def airline_list(request, template_name='airline_list.html'):
    airline = AirlineSafety.objects.all()
    data = {}
    data['object_list'] = airline
    return render(request, template_name, data)


def airline_create(request, template_name='airline_form.html'):
    form = AirlineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('airline_list')
    return render(request, template_name, {'form': form})


def airline_update(request, pk, template_name='airline_form.html'):
    airline = get_object_or_404(AirlineSafety, pk=pk)
    form = AirlineForm(request.POST or None, instance=airline)
    if form.is_valid():
        # airline_data is app_name in url.py
        return redirect('airline_list')
    return render(request, template_name, {'form': form})


def airline_delete(request, pk, template_name='airline_confirm_delete.html'):
    airline = get_object_or_404(AirlineSafety, pk=pk)
    if request.method == 'POST':
        airline.delete()
        return redirect('airline_list')
    return render(request, template_name, {'object': airline})
