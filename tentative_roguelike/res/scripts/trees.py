from msilib.schema import Binary


class BinaryTree:
    def __init__(self,root,left = None,right = None):
        self.cont = root
        self.left = left
        self.right = right

    def add_left(self,thing):
        self.left = BinaryTree(thing)
    
    def add_right(self,thing):
        self.right = BinaryTree(thing)

    def showTree(self):
        print(self.cont)
        if not (self.right is None and self.left is None):
            if self.left is not None:
                self.left.showTree()
            if self.right is not None:
                self.right.showTree()

test = BinaryTree(1,BinaryTree(2,BinaryTree(2),BinaryTree(5)))
test.showTree()
