import time

class RecommendationAlgorithm():
    def __init__(self, user, city_list, criteria, tree, hash_table):
        self.user = user
        self.city_list = city_list
        self.criteria = criteria
        self.tree = tree
        self.hash_table = hash_table

    def set_criteria(self, continent, size, is_capital):
        self.criteria = {
            'continent': continent,
            'size': size,
            'is_capital': is_capital
        }

    def get_recommendations(self):
        city_key = "None"
        print("criteria", self.criteria)
        print("city", self.city_list[0])
        print(self.city_list[0].continent)
        print(self.city_list[0].size)
        print(self.city_list[0].is_capital)
        # if is_capital is false, set the value to no

        for city in self.city_list:
            if self.criteria['continent'] == city.continent.lower() and self.criteria['size'] == city.size.lower() and self.criteria['is_capital'] == city.is_capital:
                city_key = f"{city.city_id}"
                break
            else:
                continue

        print(city_key)
        if city_key:
            # Measure time for Red-Black Tree search in milliseconds
            start_time = time.perf_counter()
            rb_tree_result = self.tree.search(city_key)
            rb_tree_time = (time.perf_counter() - start_time) * 1000  # Convert to milliseconds

            # Measure time for Hash Table search
            start_time = time.perf_counter()
            hash_table_result = self.hash_table.search(city_key)
            hash_table_time = (time.perf_counter() - start_time) * 1000  # Convert to milliseconds

            if rb_tree_result and hash_table_result:
                return {
                    'rb_tree': {
                    'time': f"{rb_tree_time:.6f} ms",
                    'City': rb_tree_result.value.name,
                    'Country': rb_tree_result.value.country,
                    'Continent': rb_tree_result.value.continent,
                    'Population': rb_tree_result.value.population,
                    'Size': rb_tree_result.value.size,
                    'Flag': rb_tree_result.value.flag,
                    'is_capital': rb_tree_result.value.is_capital
                    },
                    'hash_table': {
                        'time': f"{hash_table_time:.6f} ms",
                        'City' : hash_table_result.name,
                        'Country': hash_table_result.country,
                        'Continent': hash_table_result.continent,
                        'Population': hash_table_result.population,
                        'Size': hash_table_result.size,
                        'Flag': hash_table_result.flag,
                        'is_capital': hash_table_result.is_capital
                    }
                }
        else:
            return {"sorry, no city found" : "please try again"}
