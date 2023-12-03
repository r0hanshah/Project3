from django.shortcuts import render
import requests
from .citys_util import parse_city_data  # Make sure this is correctly imported


def home(request):
    url = 'https://parseapi.back4app.com/classes/Continentscountriescities_City?limit=10&include=country,country.continent&keys=name,country,country.name,country.emoji,country.capital,country.continent,country.continent.name,population,cityId'
    headers = {
        'X-Parse-Application-Id': 'UYc71G7r391fHhOVopWNjVyUcSAuI3seeCzw0Kn5',
        'X-Parse-REST-API-Key': 'mDIkA4mPqLMhR9oyeabWn323MOcXpdAUAHh2cuNi'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        api_data = response.json()
        # Parse the API data to get a list of City objects
        cities = parse_city_data(api_data)
        # Pass the list of City objects to the template
        return render(request, "base.html", {'data': {'results': cities}})
    else:
        return render(request, "base.html", {'data': {'error': 'Failed to fetch data'}})
