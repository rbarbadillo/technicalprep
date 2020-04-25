class Node():
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList():

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

    def prepend(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new
        self.length = + 1

    def insert(self, index, value):
        new = Node(value)
        aux = self.head
        if index >= self.length:
            self.append(value)
            return
        if index == 0:
            self.prepend(value)
            return
        for i in range(0, self.length):
            if i == index - 1:
                # Multiple assignment in Python: https://stackoverflow.com/questions/8725673/multiple-assignment-and-evaluation-order-in-python
                # Right-hand side is always evaluated fully before doing the actual setting of variables.
                aux.next, new.next = new, aux.next
                self.length += 1
                break
            aux = aux.next

    def remove(self, index):
        aux = self.head
        if index > self.length:
            print('Wrong index.')
        if index == 0:
            self.head = aux.next
            self.length -= 1
            return
        for i in range(0, self.length):
            if i == self.length - 1:
                aux.next = None
                self.tail = aux
                self.length -= 1
                break
            if i == index - 1:
                aux.next = aux.next.next
                self.length -= 1
                break
            aux = aux.next


    def printl(self):
        print('Head: { value = ' + str(self.head.data) +
              ', next = ' + str(self.head.next)+'}')
        print('Tail: { value = ' + str(self.tail.data) +
              ', next = ' + str(self.tail.next)+'}')
        print('Length: ' + str(self.length))

    def printarray(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        print('Length = '+str(self.length))


l = LinkedList()
l.append(10)
l.printl()
l.append(5)
l.printl()
l.append(6)
l.printl()
l.printarray()
l.insert(2, 20)
l.printarray()
l.remove(2)
l.printarray()
l.remove(0)
l.printarray()
