""" You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. """


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new = Node(value)
        if self.head == None:
            self.head = new
            self.tail = self.head
        else:
            # this will update the head.next chain before replacing tail
            self.tail.next = new
            self.tail = new
        self.length += 1

    def printList(self):
        aux = self.head.next
        listString = str(self.head.data)
        for _ in range(1, self.length ):
            string = '->' +  str(aux.data)
            listString = listString + string
            aux = aux.next
        return print(listString)
    
    def getitem(self, index):
        aux = self.head
        for _ in range(0, index):
            aux = aux.next
        return aux.data



# (0) Brute force approach


def addTwoNumbers(l1: LinkedList, l2: LinkedList) -> str:
    i1 = getInteger(l1)
    i2 = getInteger(l2)
    resultAsInteger = i1 + i2
    return getLinkedList(resultAsInteger).printList()

def getInteger(l: LinkedList) -> int:
    integer = 0
    for i in range(0, l.length): # O(length)
        tosum = 10**i * l.getitem(i)
        integer += tosum
    return integer

def getLinkedList(i: int) -> LinkedList:
    l = LinkedList()
    while i > 0: # O(length)
        i = i/10
        cipher = int((i - int(i)) * 10)
        l.append(cipher)
        i = int(i)
    return l

l1 = LinkedList()
l1.append(2)
l1.append(4)
l1.append(3)
l2 = LinkedList()
l2.append(5)
l2.append(6)
l2.append(4)
print(addTwoNumbers(l1, l2))

# Time complexity: O(max(l1.length, l2.length))
# Space complexity: O(max(l1.length, l2.length))