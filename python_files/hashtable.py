# in this file we will implement the hash table


class HashTable:

    def __init__(self):
        self.capacity = 10;
        self.size = 0;
        self.buckets = [0] * self.capacity
