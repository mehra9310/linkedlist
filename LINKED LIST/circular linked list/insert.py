class Node:
    def __init__(self, value= None):
        self.value = value
        self.next = None


class circularlinkedlist:
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
            

    def insert(self, value, location):
        newnode = Node(value)
        if self.curr == None:
            self.curr = newnode
            self.end = newnode
        else:
            if location == 0:
                newnode.next = self.curr
                self.curr = newnode
                self.end.next = newnode
            elif location == -1:
                newnode.next = self.curr
                #newnode.next = self.end.next
                self.end.next = newnode
                self.end = newnode
            else:
                nodetemp = self.curr
                index = 0
                while index < location-1:
                    nodetemp = nodetemp.next
                    index += 1
                #nextnode = nodetemp.next
                #nodetemp.next = newnode
                #newnode.next = nextnode
                newnode.next = nodetemp.next
                nodetemp.next = newnode

    def treverse(self):
        node1 = self.curr
        while node1:
            print(node1.value)
            node1 = node1.next
            if node1 == self.end.next:
                break

    def searching(self, value1):
        if self.curr == None:
            print("empty !!!")
        else:
            tempnode = self.curr
            index = 0
            while tempnode:
                if tempnode.value == value1:
                    return str(tempnode.value)+ " is present is index --> "+str(index)                    
                tempnode = tempnode.next
                index += 1
                if tempnode == self.end.next:
                     return "not presentin linked list"
            


    def deletion(self, location):
        if self.curr is None:
            print("linked list is empty")
        else:
            if location == 0:
                if self.curr == self.end:
                    self.curr.next = None
                    self.curr = None
                    self.end = None
                else:
                    self.curr = self.curr.next
                    self.end.next = self.curr
            if location == -1:
                if self.curr == self.end:
                    self.curr.next = None
                    self.curr = None
                    self.end = None
                else:
                    node = self.curr
                    while node is not None :
                        
                        if node.next == self.end:
                              break
                        node = node.next
                    node.next = self.curr
                    self.end = node
                
            else:
                temp = self.curr
                index = 0
                while index < location-1:
                    temp = temp.next
                    index += 1
                nextnode = temp.next
                temp.next = nextnode.next

    def deleteEntireCSLL(self):
        self.curr = None
        self.end.next = None
        self.end = None
a = circularlinkedlist()
a.insert(0, 0)
a.insert(1, -1)
a.insert(3, -1)
a.insert(2, 1)
a.insert(4, -1)
a.insert(29, 2)
a.insert(200, -1)
print([node.value for node in a])
a.treverse()
print(a.searching(200))
a.deletion(-1)
print([node.value for node in a])
a.deleteEntireCSLL()
print([node.value for node in a])
