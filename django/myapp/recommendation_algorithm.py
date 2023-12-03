import citys_util
import redblack
import hashtable
import time

class RecommendationAlgorithm():
    def __init__(self, user, city, criteria, tree, hash_table):
        self.user = user
        self.city = city
        self.criteria = criteria
        self.tree = tree
        self.hash_table = hash_table

    def set_criteria(self, continent, size, is_capital):
        self.criteria = {
            'continent': continent,
            'size': size,
            'is_capital': is_capital
        }


