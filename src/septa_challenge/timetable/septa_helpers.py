from urllib2 import urlopen, HTTPError
from urllib import quote
import json
from time import strptime


class Trip:
    def __init__(self, id, destination, sched_time, depart_time, status):
        self.id = id
        self.sched_time = sched_time
        self.depart_time = depart_time
        self.status = status
        self.on_time = self._convert_time(depart_time) <= \
            self._convert_time(sched_time)

    def _convert_time(self, timestamp):
        # ex: Jun 9 2015 12:39:00:000PM
        return strptime(timestamp.replace(':000', ' '), '%b %d %Y %I:%M:%S %p')


def _build_url(station):
    SEPTA_URL = 'http://www3.septa.org/hackathon/Arrivals/'
    sanitized_station = station.replace('Terminals', 'Terminal').replace(' & ', '-')
    return quote(SEPTA_URL + sanitized_station, safe=':/-')


def _format_response(parsed_json):
    formatted = {}
    if parsed_json['Northbound']:
        formatted['direction'] = 'Northbound'
        data = parsed_json['Northbound']
    else:
        formatted['direction'] = 'Southbound'
        data = parsed_json['Southbound']

    formatted['trips'] = [
        Trip(d['train_id'], d['destination'], d['sched_time'], d['depart_time'], d['status'])
        for d in data
    ]

    return formatted

def get_train_data(starting_station):
    url = _build_url(starting_station.name)

    try:
        response = urlopen(url)
        parsed = json.load(response)
        return _format_response(parsed.values()[0][0])
    except HTTPError, ValueError:
        return None
