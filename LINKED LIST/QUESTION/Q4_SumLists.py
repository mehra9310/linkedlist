#   Created by Elshad Karimov on 18/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Question 4 - Sum Lists

from xyz import Linked


def reverse(llA):
    current = llA.curr
    previous = None
    while current != None:
        tempnode = current.next
        current.next = previous
        previous = current
        current = tempnode

    llA.curr = previous


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


llA = Linked()
llA.generate(3, 0, 10)
print(llA)

# llA.insert(7)
# llA.insert(1)
# llA.insert(6)
reverse(llA)
#print(llA)


llB = Linked()
#llB.insert(5)
#llB.insert(9)
#llB.insert(2)
llB.generate(3, 0, 10)
print(llB)
reverse(llB)
print("sum")
#print(llB)
print(sumList(llA, llB))

