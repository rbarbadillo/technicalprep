class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.data

    def push(self, data):
        new = Node(data)
        if self.bottom == None:
            self.bottom = new
            self.top = self.bottom
            self.length = 1
        else:
            self.top.next = new
            self.top = self.top.next
            self.length += 1
    
    def pop(self):
        aux = self.bottom
        for _ in range(1, self.length - 1):
            aux = aux.next
        aux.next = None
        self.top = aux
        self.length -= 1

    def printself(self):
        print('Top: { data = ' + str(self.top.data) +
              ', next = ' + str(self.top.next)+'}')
        print('Bottom: { value = ' + str(self.bottom.data) +
              ', next = ' + str(self.bottom.next)+'}')
        print('Length: ' + str(self.length))

    def printstack(self):
        temp = self.bottom
        while temp != None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print()


mystack = Stack()
mystack.push('google')
mystack.printself()
mystack.push('microsoft')
mystack.printself()
mystack.push('apple')
mystack.printself()
mystack.printstack()
mystack.pop()
mystack.printself()
mystack.printstack()