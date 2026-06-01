class Node:
    def __init__(self, key=0, val=0):
        self.key = key 
        self.val = val 
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left 

    def insert(self, node): # insert before right dummy 
        prev_node = self.right.prev 
        prev_node.next = node 
        node.next = self.right 
        self.right.prev = node 
        node.prev = prev_node 

    def remove(self, node):
        prev_node = node.prev 
        next_node = node.next 

        prev_node.next = next_node 
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
        
        node = Node(key, value)
        self.cache[key] = node 
        self.insert(node) 

        if len(self.cache) > self.capacity:
            lru_node = self.left.next 
            self.remove(lru_node)
            del self.cache[lru_node.key]

