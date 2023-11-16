class BSTNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        '''
        Checks if this node is a new leaf and sets its' value if so.
        Otherwise, new value <= this node goes to the left, new value > this
        node goes to the right. Creates a new node if the left or right is empty.
        '''
        if self.val is None:
            self.val = val
            return
        
        if val <= self.val:
            if self.left is None:
                self.left = BSTNode(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BSTNode(val)
            else:
                self.right.insert(val)

    def search(self, val):
        '''
        Checks if this nodes value is equal to the 
        value we're searching for.  If it's not, then recurses
        on the left or right branches, until it find the value
        or hits the bottom.
        '''
        if val == self.val:
            return True
        
        if val < self.val:
            if self.left == None:
                return False
            else:
                return self.left.search(val)
        else:
            if self.right == None:
                return False
            else:
                return self.right.search(val)

    def min(self):
        if self.left is None:
            return self.val
               
        return self.left.min()

    def max(self):
        if self.right is None:
            return self.val
        
        return self.right.max()

    # def predecessor(self):

    # def successor(self):

    # def delete(self):

if __name__ == "__main__":
    nodes = [2, 3, 1, 5]
    bst = BSTNode()
    for node in nodes:
        bst.insert(node)

    print(bst.val)
    print(bst.left.val)
    print(bst.right.val)
    print(bst.search(1))
    print(bst.search(2))
    print(bst.search(6))
    print(bst.search(3))
    print(bst.search(5))
    print(bst.min())
    print(bst.max())