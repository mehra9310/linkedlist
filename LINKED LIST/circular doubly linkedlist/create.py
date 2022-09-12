class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class circulardoublylinkedlist:
    def __init__(self):
        self.curr = None
        self.end = None
    def __iter__(self):
        node = self.curr
        while node:
            yield node
            node = node.next
            if node == self.end.next:
                break 
    def create(self,value):
        newnode = Node(value)
        self.curr = newnode
        self.end = newnode
        self.next = newnode
        self.prev = newnode 
        
    def insert(self,value,location):
        newnode = Node(value)
        if self.curr == None:
            self.curr = newnode
            self.end == newnode
            self.next = None

            self.prev = None

        else:
            if location == 0:
                newnode.next = self.curr
                newnode.prev = self.end
                self.curr.prev = newnode
                self.curr = newnode
                self.end.next  = newnode
            elif location == -1:
                newnode.next = self.curr
                newnode.prev = self.end
                self.end.next = newnode
                self.end = newnode
                self.curr.prev = self.end   
                
            else:
                tempnode = self.curr
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index  += 1
                newnode.next = tempnode.next
                newnode.prev = tempnode
                tempnode.next.prev = newnode
                tempnode.next = newnode      
   
   
    def teaverse(self):
        start = self.curr
        while start:
            print(start.value)
            if start.next == self.curr:
                break
            start = start.next
   
   
    def reverse(self):
        start = self.end
        while start:
            print(start.value)
            if start.prev == self.end:
                break
            start = start.prev  
            
    def searching(self,value):
        tempnode = self.curr
        index = 0
        while tempnode:
            if tempnode.value == value:
                return str(tempnode.value)+" are present index is --> "+str(index)
            if  tempnode  == self.end:
                return " not found" 
            tempnode = tempnode.next 
            index += 1  
    
    def delete(self, location):
        if location ==0:
            self.curr = self.curr.next
            self.curr.prev = self.end 
            self.end.next = self.curr
        elif location ==-1:
            self.end = self.end.prev
            self.end.next = self.curr
            self.head.prev = self.end 
        else:
            tempnode = self.curr
            index = 0
            while index < location-1:
                tempnode = tempnode.next
                index +=1
            tempnode.next = tempnode.next.next
            tempnode.next.prev = tempnode            
    def deleteEntire(self):
        self.curr = None
        self.end.next = None
        self.end = None                                                 
        
a =  circulardoublylinkedlist()
a.create(5)
a.insert(0,0)
a.insert(1,-1)
a.insert(2,1)
a.insert(2,0)

print([node.value for node in a])  
a.teaverse()
a.reverse() 
print(a.searching(5))  
#a.delete(2)     
a.deleteEntire()
print([node.value for node in a])  
           