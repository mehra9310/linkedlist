class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Slinkedlist:
    def __init__(self):
        self.curr = None
        self.end = None

    def __iter__(self):
        node = self.curr
        while node:
            yield node
            node = node.next
# insert at the starting , between , end of the linked list


    def Insertsll(self, value, location):
        newNode = Node(value)
        if self.curr == None:
            self.curr = newNode
            self.end = newNode
        else:
            if location == 0:
                newNode.next = self.curr
                self.curr = newNode
            elif location == -1:
                newNode.next = None
                self.end.next = newNode
                #newNode = self.end 
                self.end = newNode   
            else:
                tempNode = self.curr
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                    
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                    
                if tempNode == self.end:
                    self.end = newNode
                    
     # traverse in linked list               
    def traverse(self):
        if self.curr == None:
            print("empty linked list.")
        else:
            node = self.curr
            while node:
                print(node.value)
                node = node.next
                
 #  searching in linked list...               
    def searching(self,valuenode):
        if self.curr == None:
            return "the list not exist"
        else:
            node = self.curr
            while node != None:
                if node.value == valuenode:
                    return  node.value
                node = node.next
               
            return "the node not found."       
#  delete in linked list......add()
    def deletesll(self,location):
        if self.curr ==0:
            return "list are not present"
        else:
            if location == 0:
                if self.curr == self.end:
                    self.curr = None
                    self.end = None
                else:
                    self.curr = self.curr.next
            elif location == -1:
                if self.curr == self.end:
                    self.curr = None
                    self.end = None
                else:
                    node = self.curr
                    while node !=0:
                        if node.next == self.end:
                            break
                        node = node.next
                    node.next = None
                    self.end = None   
            else:
                tempnode = self.curr
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index += 1
                nextNode = tempnode.next
                tempnode.next = nextNode.next
    def reverse(sel):
       current = sel.curr
       previous = None
       while current != None:
           tempnode = current.next
           current.next = previous
           previous = current
           current = tempnode
           print(previous.value)            
                    
                                
                                      
                            
    
singlylinkedlist = Slinkedlist()
singlylinkedlist.Insertsll(1, 1)
singlylinkedlist.Insertsll(1, 1)
singlylinkedlist.Insertsll(3, 1)
singlylinkedlist.Insertsll(1,1)
singlylinkedlist.Insertsll(5, -1)
singlylinkedlist.Insertsll(0, 2)
print([node.value for node in singlylinkedlist])
#singlylinkedlist.traverse()
#print(singlylinkedlist.searching(5))
#singlylinkedlist.deletesll(0)
singlylinkedlist.reverse()
#print([node.value for node in singlylinkedlist])
