class node:
    def __init__(self,value = None):
        self.value = value
        self.next = None
        
class slinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
   
singlylinkedlist = slinkedlist()
node1 = node(1)
node2 = node(2)

singlylinkedlist.head = node1
singlylinkedlist.head.next = node2
singlylinkedlist.next = node2        
                