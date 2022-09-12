from xyz import Linked


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


a = Linked()
a.generate(10, 0, 99)
print(a)
# remone(b)
removeDups1(a)
print(a)
  