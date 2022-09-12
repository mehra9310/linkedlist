
from xyz import Linked , Node
def intersection(llA ,llB):
    if llA.end is not llB.end:
        return False
    
    lenA = len(llA)
    lenB = len(llB)
     
    shorter = llA if lenA<lenB else llB
    longer = llB if lenA<lenB else llA
    
    diff = len(llA)-len(llB)
    longernode = longer.curr
    shorternode = shorter.curr 
    for i in range(diff):
        longernode = longernode.next
     
    while shorternode !=  longernode:
        longernode = longernode.next
        shorternode = shorternode.next
        
    return shorternode

def addsamenode(llA,llB,value):
    tempnode = Node(value)
    llA.end.next = tempnode
    llA.end = tempnode
    llB.end.next = tempnode
    llB.end = tempnode
    
llA = Linked()    
llA.generate(5,0,10)

llB = Linked()    
llB.generate(5,0,10)


addsamenode(llA,llB,110)
addsamenode(llA,llB,14)

print(llA)
print(llB)

print(intersection(llA,llB))
       
        