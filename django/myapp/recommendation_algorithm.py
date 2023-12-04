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
        city_key = None
        for city in self.city_list:
            if (city.size == self.criteria['size'] and 
                city.continent == self.criteria['continent'] and 
                city.is_capital == self.criteria['is_capital']):
                city_key = f"{city.name}-{city.country}"
                break

        if city_key:
            # Measure time for Red-Black Tree search
            start_time = time.time()
            rb_tree_result = self.tree.search(city_key)
            rb_tree_time = time.time() - start_time

            # Measure time for Hash Table search
            start_time = time.time()
            hash_table_result = self.hash_table.search(city_key)
            hash_table_time = time.time() - start_time

            return {
                'rb_tree': {
                    'time': rb_tree_time,
                    'result': rb_tree_result
                },
                'hash_table': {
                    'time': hash_table_time,
                    'result': hash_table_result
                }
            }
        else:
            return None
