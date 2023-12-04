from django.shortcuts import render
import requests
import random
from .citys_util import parse_city_data  # Make sure this is correctly imported
from .citys_util import load_data_into_structures  # Make sure this is correctly imported
from .redblack import RedBlackTree
from .hashtable import HashTable
from django.http import JsonResponse
from .recommendation_algorithm import RecommendationAlgorithm


def home(request):
    url = 'https://parseapi.back4app.com/classes/Continentscountriescities_City?limit=1000&include=country,country.continent&keys=name,country,country.name,country.emoji,country.capital,country.continent,country.continent.name,population,cityId'
    headers = {
        'X-Parse-Application-Id': 'UYc71G7r391fHhOVopWNjVyUcSAuI3seeCzw0Kn5',
        'X-Parse-REST-API-Key': 'mDIkA4mPqLMhR9oyeabWn323MOcXpdAUAHh2cuNi'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        api_data = response.json()
        # Parse the API data to get a list of City objects
        global recommendation_algorithm
        cities = parse_city_data(api_data)
        rb_tree = RedBlackTree()
        hash_table = HashTable()
        load_data_into_structures(cities, rb_tree, hash_table)

        # randomize the list of cities
        random.shuffle(cities)
        # create an instance of the recommendation algorithm
        recommendation_algorithm = RecommendationAlgorithm(request.user, cities, None, rb_tree, hash_table)
        # Pass the list of City objects to the template
        return render(request, "base.html", {'data': {'results': cities}})
    else:
        return render(request, "base.html", {'data': {'error': 'Failed to fetch data'}})

def get_recommendation(request):
    # Extract criteria from the request
    continent = request.GET.get('continent')
    size = request.GET.get('size')
    is_capital = request.GET.get('is_capital') == 'true'

    global recommendation_algorithm

    recommendation_algorithm.set_criteria(continent, size, is_capital)
    recommendations = recommendation_algorithm.get_recommendations()

    
    if recommendations:
        return JsonResponse(recommendations)
    else:
        return JsonResponse({"sorry, no city found" : "please try again"})
    
