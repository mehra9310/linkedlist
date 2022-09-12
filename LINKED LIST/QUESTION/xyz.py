from random import randint


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class Linked:
    def __init__(self):
        self.curr = None
        self.end = None

    def __iter__(self):
        node = self.curr
        while node:
            yield node
            node = node.next
    # print the nodes. method 1
    def __str__(self):
        values = [str(x.value) for x in self]
        return '-->'.join(values)
    
    
    def printll(self):
        values = [str(x.value) for x in self]
        print(' --> '.join(values))
    

    def __len__(self):
        index = 0
        node = self.curr
        while node:
            index += 1
            node = node.next
        return index

    def insert(self, value):
        newnode = Node(value)
        if self.curr == None:
            self.curr = newnode
            self.end = newnode
        else:
            self.end.next = newnode
            self.end = newnode
        return self.end

    def generate(self, n, min_value, max_value):
        self.curr = None
        self.end = None
        for i in range(n):
            self.insert(randint(min_value, max_value))
        return self


a = Linked()
#a.generate(10, 0, 99)
##print(a)
#print(len(a))
#a.printll()
