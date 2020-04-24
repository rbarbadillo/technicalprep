class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new = Node(value)
        if self.root == None:
            self.root = new
            return
        else:
            currentnode = self.root
            while True:
                # Right
                if value > currentnode.value:
                    if currentnode.right == None:
                        currentnode.right = new
                        return
                    else:
                        currentnode = currentnode.right
                # Left
                elif value < currentnode.value:
                    if currentnode.left == None:
                        currentnode.left = new
                        return
                    else:
                        currentnode = currentnode.left
    def lookup(self, value):
        currentnode = self.root
        while True:
            if currentnode == None:
                return False
            elif currentnode.value == value:
                return True
            elif value < currentnode.value:
                currentnode = currentnode.left
            else:
                currentnode = currentnode.right

bst = BinarySearchTree()
bst.insert(8)
bst.insert(10)
bst.insert(5)
bst.insert(7)
bst.insert(20)
bst.lookup(5)