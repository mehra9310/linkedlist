class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Circularlinkedlist:
    def __init__(self):
        self.curr = None
        self.end = None
        
    def __iter__(self):
        node = self.curr
        while node:
            yield node
            if node.next == self.curr:
                break
            node = node.next
            
    def create(self,value):
        newnode = Node(value)
        newnode.next = newnode
        self.curr = newnode
        self.end = newnode
        return "created"  
    
a = Circularlinkedlist()
a.create(1)
print([node.value for node in a])          
            
            
                        