from xyz import Linked

def kthvaluefinf(self,n):
    pointer1 = self.curr
    pointer2 = self.curr
    for i in range(n):
        pointer2 = pointer2.next
        #print( pointer2  )  
    while pointer2:
        pointer1 = pointer1.next    
        pointer2 = pointer2.next
        #print(pointer1)
    return pointer1

a = Linked()
a.generate(10,0,99)

a.printll()
print(kthvaluefinf(a,4))    
