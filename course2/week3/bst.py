class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if root is None:
            return Node(val)

        # Val less than root goes to left subtree
        # Val greater than current root goes to right subtree
        if val < root.val:
            root.left = self._insert(root.left, val)
        elif val > root.val:
            root.right = self._insert(root.right, val)

        return root

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, root, val):
        if root is None or root.val == val:
            return root
        
        # Recursively search in left/right subtree
        if val < root.val:
            return self._search(root.left, val)
        elif val > root.val:
            return self._search(root.right, val)

    def min(self):
        return self._min(self.root)

    def _min(self, root):
        # Continue down left subtrees until it hits a leaf
        if root.left is None:
            return root.val
        
        return self._min(root.left)

    def max(self):
        return self._max(self.root)

    def _max(self, root):
        # Continue down right subtrees until it hits a leaf
        if root.right is None:
            return root.val
        
        return self._max(root.right)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, root, val):
        if root is None:
            return None
        
        # Search for val by recursing on left/right subtree,
        # store the child pointer
        if val < root.val:
            root.left = self._delete(root.left, val)
        elif val > root.val:
            root.right = self._delete(root.right, val)
        else:
            # Found val: if val has 0 or 1 children, then return a pointer to it
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
        
            # val has 2 children, replace with minimum val from right subtree
            root.val = self._min(root.right)
            root.right = self._delete(root.right, root.val)

        return root

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.val)
            self._inorder_traversal(root.right, result)
        
# Example usage
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print("Inorder traversal:", bst.inorder_traversal())

bst.delete(20)
print("Inorder traversal after deleting 20:", bst.inorder_traversal())
bst.delete(20)
search_result = bst.search(40)
if search_result:
    print(f"Node with key 40 found in the tree.")
else:
    print(f"Node with key 40 not found in the tree.") 
