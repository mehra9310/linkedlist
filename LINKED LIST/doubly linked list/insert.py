class Node:
    def __init__(self, value):
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

    def create(self, value):
        node = Node(value)
        self.curr = node
        self.next = None
        self.prev = None
        self.end = node

    def insert(self, value, location):
        newnode = Node(value)
        if self.curr == None:
            self.curr = newnode
            self . end = newnode
            #self.prev = None
            #self.next = None
        else:
            if location == 0:
                newnode.next = self.curr
                newnode.prev = None
                self.curr.prev = newnode
                self.curr = newnode
            elif location == -1:
                newnode.next = None
                newnode.prev = self.end
                self.end.next = newnode
                self.end = newnode
            else:
                tempnode = self.curr
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index += 1
                newnode.next = tempnode.next
                newnode.prev = tempnode
                tempnode.next = newnode
                tempnode.next.prev = newnode

    def traverse(self):
        if self.curr == None:
            print("empty!!!!???")
        else:
            tempnode = self.curr
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next
            print(" ")

    def terverseReverse(self):
        insert = self.end
        while insert:
            print(insert.value)
            insert = insert.prev

    def search(self, value):
        temp = self.curr
        index = 0
        while temp:
            if temp.value == value:
                return str(temp.value)+" are lies on index -->"+str(index)
            index += 1
            temp = temp.next
        return "not found"

    def deleteNode(self, location):
        if self.curr is None:
            print("There is not any element in DLL")
        else:
            if location == 0:
                if self.curr == self.end:
                    self.curr = None
                    self.end = None
                else:
                    self.curr = self.curr.next
                    self.curr.prev = None
            elif location == -1:
                if self.curr == self.end:
                    self.curr = None
                    self.end = None
                else:
                    self.end = self.end.prev
                    self.end.next = None
            else:
                curNode = self.curr
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")


a = Doublylinkedlist()
# a.create(5)
#print([node.value for node in a])
a.insert(0, 0)
a.insert(1, -1)
a.insert(50, 1)
a.insert(9, 2)
a.insert(2, -1)
print([node.value for node in a])
#a.traverse()
#a.terverseReverse()
#print(a.search(50))
a.deleteNode(-1)
print([node.value for node in a])
