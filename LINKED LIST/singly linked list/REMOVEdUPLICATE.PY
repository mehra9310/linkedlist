
# NOTE :
 #REMOVE DUPLICATE IN THE GIVEN LINKEDLIST 


from insertpractic import Slinkedlist


def remone(ll):
    if ll.curr is None:
        return
    else:
        currentnode = ll.curr
        visited = set([currentnode.value])
        while currentnode.next:
            if currentnode.next.value in visited:
                currentnode.next = currentnode.next.next
            else:
                visited.add(currentnode.next.value)
                currentnode = currentnode.next
        return ll

# ALERNATE METHOD.........add()
def removeDups1(ll):

    currentNode = ll.curr
    while currentNode:
        runner = currentNode
        while runner.next:
            if runner.next.value == currentNode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentNode = currentNode.next
    return ll.curr


a = Slinkedlist()
a.Insertsll(10,0)
a.Insertsll(9,-1)
a.Insertsll(11,-1)
a.Insertsll(9,1)
a.Insertsll(7,0)
a.Insertsll(1,2)
a.Insertsll(7,3)
print(a)
#print([node.value for node in a])
remone(a)
#removeDups1(a)
#print([node.value for node in a])
print(a)

