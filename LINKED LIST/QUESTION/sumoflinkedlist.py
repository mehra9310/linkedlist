
from xyz import Linked


def sumofadd(llA,llB):
    
    def reverse(self):
        current = self.curr
        previous = None
        while current != None:
            tempnode = current.next
            current.next = previous
            previous = current
            current = tempnode
            
        self.curr = previous
        llA = reverse(llA)
        llB = reverse(llB)
        ans  = adddd(llA,llB)
        ans = reverse(ans)
        
    def adddd(llA, llB):
        
        n1 = llA.curr
        n2 = llB.curr
        carry = 0
        llC = Linked()
        while n1!= None or n2 != None:
            sum = carry
            if n1:
                sum += n1.value
                n1 = n1.next
            if n2:
                sum += n2.value
                n2 = n2.next
            llC.adds(int(sum % 10))
            carry = sum/10
    
        return llC
        
    
llA     = Linked()
llA.    generate(3,0,6)
#llA    .add(8)
#llA.add(9)

llB = Linked()
llB.generate(3,0,6)
#llB.add(7)
#llB.add(8)
print(llA)
print(llB)
print(sumofadd(llA,llB))
