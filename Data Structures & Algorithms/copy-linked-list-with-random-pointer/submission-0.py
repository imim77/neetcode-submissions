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
        mapa = {None : None}

        curr = head
        while curr:
            mapa[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = mapa[curr]
            copy.next = mapa[curr.next]
            copy.random = mapa[curr.random]
            curr = curr.next
        
        return mapa[head]