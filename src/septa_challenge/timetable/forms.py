from django import forms

from . models import Station


class StationSelectForm(forms.Form):
    station_names = [(s.id, s.name) for s in Station.objects.all()]

    starting_station = forms.ChoiceField(choices=station_names)
    ending_station = forms.ChoiceField(choices=station_names)
