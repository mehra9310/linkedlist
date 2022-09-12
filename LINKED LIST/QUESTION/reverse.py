from xyz import Linked

# reverse the list..
def reverse(self):
    current = self.curr
    previous = None
    while current != None:
        tempnode = current.next
        current.next = previous
        previous = current
        current = tempnode
        
    self.curr = previous

def sumList(llA, llB):
    n1 = llA.curr
    n2 = llB.curr
    carry = 0
    ll = Linked()

    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.insert(int(result % 10))
        carry = result / 10

    return ll
   
a = Linked()
a.generate(10,0,99)  
#a.insert(6)  
#a.insert(8)  
#a.insert(5)  
#a.insert(2)  
print(a)
reverse(a)
print(a)
   
    