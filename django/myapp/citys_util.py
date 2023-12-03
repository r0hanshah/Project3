import requests

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
        population = item.get('population')

        country_data = item.get('country')
        if country_data:
            country = country_data.get('native', None)
            capital = country_data.get('capital', None)
            continent = country_data['continent']['name'] if country_data.get('continent') else None
            flag = country_data.get('emoji', None)
            is_capital = (name == capital)
        else:
            country, continent, flag, is_capital = None, None, None, False

        # Determine city size based on population
        if population <= 100000:
            size = "Small"
        elif 100000 < population < 600000:
            size = "Medium"
        else:
            size = "Large"

        city = City(city_id, name, country, population, continent, flag, is_capital, size)
        cities.append(city)
    return cities



def load_data_into_structures(cities, rb_tree, hash_table):
    for city in cities:
        key = f"{city.name}-{city.country}"  # Unique key, adjust as needed
        rb_tree.insert(key, city)
        hash_table[key] = city
