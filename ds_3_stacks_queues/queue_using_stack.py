# Implementation of a queue using a stack (built with an array)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.arr = []
        self.length = 0

    def push(self, data: int) -> None:
        self.arr.append(data)
        self.length += 1

    def pop(self) -> int:
        poppeditem = self.arr[self.length - 1]
        del self.arr[self.length - 1]
        self.length -= 1
        return poppeditem

    def peek(self) -> int:
        return self.arr[self.length - 1]

    def is_empty(self) -> bool:
        if self.length == 0:
            return True
        return False


class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, data: int) -> None:
        self.inbox.push(data)

    def dequeue(self) -> int:
        self.updateoutbox()
        return self.outbox.pop()

    def peek(self) -> int:
        self.updateoutbox()
        return self.outbox.peek()

    def is_empty(self) -> bool:
        return self.inbox.is_empty() and self.outbox.is_empty()
    
    def updateoutbox(self) -> None:
       if self.outbox.is_empty():
            while not self.inbox.is_empty():
                popped = self.inbox.pop()
                self.outbox.push(popped)


q = Queue()
q.enqueue(0)
q.enqueue(1)
print(q.dequeue())
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.inbox.arr)
print(q.outbox.arr)
print(q.peek())