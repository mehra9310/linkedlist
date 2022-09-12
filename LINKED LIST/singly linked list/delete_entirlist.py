class Node:
    def __init__(self, value):
        self.val = value
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
# insert

    def insertsll(self, value, location):
        newnode = Node(value)
        if self.curr == None:
            self.curr = newnode
            self.end = newnode
        else:
            if location == 0:
                newnode.next = self.curr
                self.curr = newnode
            elif location - 1:
                newnode.next = None
                self.end.next = newnode
                self.end = newnode
            else:
                tempnode = self.curr
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                newtemp = tempnode.next
                tempnode.next = newnode
                newnode.next = newtemp
                if tempnode == self.end:
                    self.end = newnode
    def alldilite(self):
        if self.curr == None:
            print("no list are found")
        else:
            self.curr = None
            self.end = None    

a = Slinkedlist()
a.insertsll(1, 1)
a.insertsll(1, 1)
a.insertsll(3, 1)
a.insertsll(1, 1)
a.insertsll(5, 1)
a.insertsll(0, 0)
print([node.val for node in a])
a.alldilite()
print([node.val for node in a])

