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
        self.load_factor = 0.75


    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get_index(self, key):
        return hash(key) % self.capacity; # this will give us the index of the key

    def insert(self, key, value):

        # if load factor is greater than 0.75, double the capacity
        if self.size / self.capacity > self.load_factor:
            self.resizeAndHash()

        bucketIndex = self.get_index(key)

        # if the bucket is empty, insert the key-value pair
        if self.buckets[bucketIndex] == 0:
            self.buckets[bucketIndex] = self.Node(key, value)
            self.size += 1
            return

        # if the bucket is not empty, we need to check if the key already exists
        current_node = self.buckets[bucketIndex]
        while current_node.next:  # Stop at the last node
            if current_node.key == key:
                current_node.value = value
                return
            current_node = current_node.next

        # Add new node at the end of the list
        new_node = self.Node(key, value)
        current_node.next = new_node
        self.size += 1



    def search(self, key):
        bucketIndex = self.get_index(key)

        current_node = self.buckets[bucketIndex];

        # iterates through linked list looking for key
        while current_node:
            # if current node's key matches searched key, return current node's value 
            if current_node.key == key:
                return current_node.value
            
            #moves pointer to next node in linked list
            current_node= current_node.next

        # returns -1 if not found
        return -1; 

    def delete(self,key):
        bucketIndex = self.get_index(key);

        current_node = self.buckets[bucketIndex];
        previous_node = None;

        while current_node:
            # delete current node if key found
            if current_node.key == key:

                # if previous node exists
                if(previous_node):
                    previous_node.next = current_node.next
                # if no nodes in bucket
                else:
                    self.buckets[bucketIndex] = None
            
                #decrements size
                self.size -= 1
                return
            

            previous_node = current_node
            current_node = current_node.next


        # returns -1 if node not found
        return -1;


    def resizeAndHash(self):
        newCapacity = self.capacity * 2;
        newBuckets = [0] * newCapacity;

        for i in range(self.capacity):
            current = self.buckets[i]
            while current:
                bucketIndex = hash(current.key) % newCapacity
                newNode = self.Node(current.key, current.value)
                newNode.next = newBuckets[bucketIndex]
                newBuckets[bucketIndex] = newNode
                current = current.next

        self.buckets = newBuckets;
        self.capacity = newCapacity;
                


                
    


    #sources: https://www.geeksforgeeks.org/separate-chaining-collision-handling-technique-in-hashing/