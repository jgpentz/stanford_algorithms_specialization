class Node:
    def __init__(self, key, color='red'):
        self.key = key
        self.left = self.right = self.parent = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='black')  # NIL sentinel node
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key)
        self._insert(new_node)

    def _insert(self, z):
        y = None
        x = self.root

        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.NIL
        z.right = self.NIL
        z.color = 'red'
        self._insert_fixup(z)

    def _insert_fixup(self, z):
        while z.parent and z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self._left_rotate(z.parent.parent)

        self.root.color = 'black'

    def delete(self, key):
        z = self._search(self.root, key)
        if z != self.NIL:
            self._delete(z)

    def _delete(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._min_value_node(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'black':
            self._delete_fixup(x)

    def _delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self._right_rotate(x.parent)
                    x = self.root

        x.color = 'black'

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _min_value_node(self, node):
        current = node
        while current.left != self.NIL:
            current = current.left
        return current

    def _search(self, root, key):
        if root == self.NIL or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NIL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root != self.NIL:
            self._inorder_traversal(root.left, result)
            result.append((root.key, root.color))
            self._inorder_traversal(root.right, result)

# Example usage:
rb_tree = RedBlackTree()
keys = [50, 30, 70, 10, 40, 60, 80]

# Insert keys
for key in keys:
    rb_tree.insert(key)

print("Inorder Traversal after insertion:")
print(rb_tree.inorder_traversal())

# Delete a key
rb_tree.delete(40)

print("Inorder Traversal after deletion of 40:")
print(rb_tree.inorder_traversal())