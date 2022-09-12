from urllib.parse import _NetlocResultMixinStr
from xyz import Linked


def partation(self, x):
    curnode = self.curr
    self.end = self.curr
    while curnode != None:
        nex = curnode.next
        #curnode.next = None
        if curnode.value < x:
            curnode.next = self.curr
            self.curr = curnode
        else:
            self.end.next = curnode
            self.end = curnode
        curnode = nex
        

    if self.end.next is not None:
        self.end.next = None


a = Linked()
# a.generate(10,0,99)
a.insert(55)
a.insert(10)
a.insert(61)
a.insert(12)
a.insert(45)
a.insert(11)
a.printll()
partation(a, 30)
a.printll()
