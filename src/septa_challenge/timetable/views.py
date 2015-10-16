from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView

from forms import StationSelectForm
from models import Station
from septa_helpers import get_train_data

# def home(request):
#     form = StationSelectForm()
#     return render(request, 'main.html', {'form': form})


def schedules(request, station_name=None):
    station, errors, schedule = None, None, None

    if request.method == 'POST':
        form = StationSelectForm(request.POST)

        if form.is_valid():
            starting_station_id = form.cleaned_data['starting_station']
            starting_station = Station.objects.filter(id=starting_station_id).first()
            schedule = get_train_data(starting_station)
            if schedule is None:
                errors = 'Could not reach SEPTA API server.'
            station = starting_station.name
        else:
            errors = 'Invalid station name(s).'
    else:
        form = StationSelectForm()

    context = {
        'form': form,
        'station': station,
        'errors': errors,
        'schedule': schedule
    }
    return render(request, 'main.html', context)
