"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None: None}

        cur = head
        while cur:
            node_copy = Node(cur.val)
            nodes[cur] = node_copy
            cur = cur.next 

        cur = head
        while cur:
            node_copy = nodes[cur]
            node_copy.next = nodes[cur.next]
            node_copy.random = nodes[cur.random]
            cur = cur.next 
        return nodes[head]




