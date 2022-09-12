class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class Doublylinkedlist:
    def __init__(self):
        self.curr = None
        self.end = None
    def __iter__(self):
        node = self.curr
        while node:
            yield node
            node = node.next
    def create(self,value):
        node = Node(value)
        self.curr = node
        self.next = None
        self.prev = None
        self.end = node

a = Doublylinkedlist() 
a.create(5)
print([node.value for node in a])               