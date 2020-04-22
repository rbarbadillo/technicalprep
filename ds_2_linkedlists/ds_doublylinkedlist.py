class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            self.length += 1

    def prepend(self, data):
        new = Node(data)
        self.head.prev = new
        new.next = self.head
        self.head = new
        self.length += 1

    def insert(self, index, data):
        if index > self.length:
            print('Index out of range')
            return
        if index == 0:
            self.prepend(data)
            return
        if index == self.length - 1:
            self.append(data)
            return
        else:
            new = Node(data)
            leader = self.traversetoindex(index)
            holder = leader.next
            leader.next = new
            new.next = holder
            holder.prev = new
            new.prev = leader
            self.length += 1

    def traversetoindex(self, index):
        currentnode = self.head
        for _ in range(index - 1):
            currentnode = currentnode.next
        return currentnode

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return
        if index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        leader = self.traversetoindex(index)
        nodeToRemove = leader.next
        holder = nodeToRemove.next
        leader.next = holder
        holder.prev = leader
        self.length -= 1

    def printarray(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        print('Length ' + str(self.length))


d = DoublyLinkedList()
d.append(19)
d.append(2)
d.append(6)
d.printarray()
d.prepend(13)
d.printarray()
d.insert(3, 122)
d.printarray()
d.remove(1)
d.printarray()