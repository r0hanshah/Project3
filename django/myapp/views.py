from django.shortcuts import render, HttpResponse
from .hashtable import HashTable
from .redblack import RedBlackTree
from .citys_util import * 
import json
import urllib
import requests

rb_tree = RedBlackTree()
hash_table = HashTable()



# Create your views here.
def home(request):


    url = 'https://parseapi.back4app.com/classes/Continentscountriescities_City?limit=10&order=cityId'
    headers = {
        'X-Parse-Application-Id': 'UYc71G7r391fHhOVopWNjVyUcSAuI3seeCzw0Kn5',
        'X-Parse-REST-API-Key': 'mDIkA4mPqLMhR9oyeabWn323MOcXpdAUAHh2cuNi'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
    else:
        data = {'error': 'Failed to fetch data'}
    return render(request, "base.html", {'data': data})
