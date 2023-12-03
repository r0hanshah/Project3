#in this file we will implement the red black tree 

class RedBlackTree:
    #  red will be true, black will be false
    class Node:
        def __init__(self, key, value):
            # city id will be key
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.color = True
            self.parent = None


    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, key, value):
        newNode = self.Node(key, value)
        newNode.color = True  # starts off red
        newNode_parent = None
        newNode_left = None
        newNode_right = None

        parent = None
        current = self.root
        while current:
            parent = current
            if newNode.key < current.key:
                current = current.left
            elif newNode.key > current.key:
                current = current.right
            else:
                return

        newNode.parent = parent
        if parent is None:
            self.root = newNode
        elif newNode.key < parent.key:
            parent.left = newNode
        else:
            parent.right = newNode

        self.balance(newNode)

    def leftRotation(self, node):
        right = node.right
        node.right = right.left
        if right.left is not None:
            right.left.parent = node

        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        
        right.left = node
        node.parent = right
    
    def rightRotation(self, node):

        left = node.left
        node.left = left.right
        if left.right is not None:
            left.right.parent = node

        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        
        left.right = node
        node.parent = left

    
    def balance(self, node):
        while node.parent.color == True and node != self.root:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left
                if uncle.color == True:
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rightRotation(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self.leftRotation(node.parent.parent)
            else:
                uncle = node.parent.parent.right
                if uncle.color == True:
                    node.parent.color = False
                    uncle.color = False
                    node.parent.parent.color = True
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.leftRotation(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self.rightRotation(node.parent.parent)
        self.root.color = False



