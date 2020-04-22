# As found here: https://github.com/theja-m/Data-Structures-and-Algorithms/blob/master/Data%20Structures%20-%20Hashtables/Hash%20Table%20Implementation.py
from random import randint


class Hashtable():
    def __init__(self, size):
        self.size = size
        self.mydict = ['None']*size
        self.addr_list = []

    def __str__(self):
        return str(self.__dict__)

    def _hash(self):
        while True:
            x = randint(0, self.size-1)
            if x not in self.addr_list:
                return x

    def set(self, key, value):
        address = self._hash()
        self.mydict[address] = [key, value]
        self.addr_list.append(address)

    def get(self, key):
        for pair in self.mydict:
            if pair[0] == key:
                return pair

    def keys(self):
        key_arr = []
        for i in self.addr_list:
            key_arr.append(self.mydict[i][0])
        return key_arr


h = Hashtable(50)
h.set('grapes', 1000)
h.set('apples', 10)
h.set('oranges', 300)
h.set('bananas', 200)
x = h.get('grapes')
key_arr = h.keys()
print(h)
print(x)
print(key_arr)
print(h.get('apples'))
