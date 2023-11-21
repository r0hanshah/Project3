# in this file we will implement the hash table
# we will be using seperate chaining to handle collisions

class HashTable:

     # nodes for linked list within hash table, used for seperate chaining
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def __init__(self):
        # inital cap will be 10, will update as needed
        self.capacity = 10;
        self.size = 0;
        self.buckets = [0] * self.capacity


    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def hash(self, key):
        return hash(key) % self.capacity; # this will give us the index of the key

    def insert(self, key, value):
        i = self.hash(key); 
    
        # if the bucket is empty, insert the key value pair
        if self.buckets[i] == 0:
            self.buckets[i] = self.Node(key, value)
            self.size += 1

        # if the bucket is not empty, we need to check if the key already exists
        if (self.buckets[i] != 0):
            # if the key already exists, add node to the end of the linked list
            current_node = self.buckets[i]
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    return
                current_node = current_node.next
            # if bucket is not empty and key does not already exist, add new node to bucket at the end of the list
            new_node = self.Node(key,value)
            current_node.next = new_node;
            self.buckets[i] = new_node
            self.size+=1


    def search(self, key):
        i = self.hash(key)

        current_node = self.buckets[i];

        # iterates through linked list looking for key
        while current_node:
            # if current node's key matches searched key, return current node's value 
            if current_node.key == key:
                return current_node.value
            
            #moves pointer to next node in linked list
            current_node= current_node.next

        # returns -1 if not found
        return -1; 



                
    


    