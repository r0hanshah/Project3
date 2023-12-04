import requests
import json

class City:
    def __init__(self, city_id, name, country, population, continent, flag, is_capital, size):
        self.city_id = city_id
        self.name = name
        self.country = country
        self.population = population
        self.continent = continent
        self.flag = flag
        self.is_capital = is_capital
        self.size = size

    def __repr__(self):
        return f"City(ID: {self.city_id}, Name: {self.name}, Country: {self.country}, Size: {self.size})"

def to_dict(self):
        return {
            "city_id": self.city_id,
            "name": self.name,
            "country": self.country,
            "population": self.population,
            "continent": self.continent,
            "flag": self.flag,
            "is_capital": self.is_capital,
            "size": self.size
        }

def fetch_data_from_api(url, app_id, rest_api_key):
    headers = {
        'X-Parse-Application-Id': app_id,
        'X-Parse-REST-API-Key': rest_api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def parse_city_data(api_data):
    cities = []
    for item in api_data['results']:
        city_id = item.get('cityId')
        name = item.get('name')

        country_data = item.get('country')
        if country_data:
            country = country_data.get('name', None)
            capital = country_data.get('capital', None)
            flag = country_data.get('emoji', None)
            is_capital = (name == capital)

            # Extracting continent name from the continent pointer object
            continent_pointer = country_data.get('continent')
            continent = continent_pointer['name'] if continent_pointer else None
        else:
            country, capital, continent, flag, is_capital = None, None, None, None, False
        population = item.get("population")

        size = "Large" if population >= 600000 else "Medium" if population > 100000 else "Small"

        city = City(city_id, name, country, population, continent, flag, is_capital, size)
        cities.append(city)
    return cities






def load_data_into_structures(cities, rb_tree, hash_table):
    for city in cities:
        key = f"{city.city_id}"  # Unique key, adjust as needed
        rb_tree.insert(key, city)
        hash_table.insert(key, city);
