from django.shortcuts import render
import requests
from .citys_util import parse_city_data  # Make sure this is correctly imported
from .citys_util import load_data_into_structures  # Make sure this is correctly imported
from .redblack import RedBlackTree
from .hashtable import HashTable
from django.http import JsonResponse
from .recommendation_algorithm import RecommendationAlgorithm


def home(request):
    url = 'https://parseapi.back4app.com/classes/Continentscountriescities_City?limit=250&include=country,country.continent&keys=name,country,country.name,country.emoji,country.capital,country.continent,country.continent.name,population,cityId'
    headers = {
        'X-Parse-Application-Id': 'UYc71G7r391fHhOVopWNjVyUcSAuI3seeCzw0Kn5',
        'X-Parse-REST-API-Key': 'mDIkA4mPqLMhR9oyeabWn323MOcXpdAUAHh2cuNi'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        api_data = response.json()
        # Parse the API data to get a list of City objects
        cities = parse_city_data(api_data)
        rb_tree = RedBlackTree()
        hash_table = HashTable()
        load_data_into_structures(cities, rb_tree, hash_table)

        #store in session
        request.session['cities'] = cities
        request.session['rb_tree'] = rb_tree
        request.session['hash_table'] = hash_table
        # Pass the list of City objects to the template
        return render(request, "base.html", {'data': {'results': cities}})
    else:
        return render(request, "base.html", {'data': {'error': 'Failed to fetch data'}})

def get_recommendation(request):
    # Extract criteria from the request
    continent = request.GET.get('continent')
    size = request.GET.get('size')
    is_capital = request.GET.get('is_capital') == 'true'

    # Retrieve from session or global storage
    rb_tree = request.session.get('rb_tree')
    hash_table = request.session.get('hash_table')

    if rb_tree is None or hash_table is None:
        return JsonResponse({'error': 'Data structures not initialized'}, status=500)

    algorithm = RecommendationAlgorithm(request.user, None, None, rb_tree, hash_table)
    algorithm.set_criteria(continent, size, is_capital)
    recommendations = algorithm.get_recommendations()

    if recommendations:
        return JsonResponse(recommendations)
    else:
        return JsonResponse({'error': 'No matching city found'}, status=404)
