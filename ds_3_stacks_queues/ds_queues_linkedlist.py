# Taken from: https://github.com/theja-m/Data-Structures-and-Algorithms/blob/master/Data%20Structures%20-%20Stacks%20and%20Queues/Queue%20using%20Linked%20List.py
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.val

    def enqueue(self, val):
        new_node = Node(val)
        if self.first == None:
            self.first = new_node
            self.last = self.first
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    def dequeue(self):
        temp = self.first.next
        if temp == None:
            self.first = None
            self.length -= 1
            return
        self.first.next = None
        self.first = temp
        self.length -= 1

    def printt(self):
        temp = self.first
        while temp != None:
            print(temp.val, end='->')
            temp = temp.next
        print()
        print(self.length)


myq = Queue()
myq.enqueue('google')
myq.enqueue('microsoft')
myq.enqueue('facebook')
myq.enqueue('apple')
myq.printt()
myq.dequeue()
myq.printt()
x = myq.peek()
print(x)
