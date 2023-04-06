class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = AVLNode(data)
        else:
            self.root = self._insert(data, self.root)

    def _insert(self, data, node):
        if not node:
            return AVLNode(data)
        elif data < node.data:
            node.left = self._insert(data, node.left)
        else:
            node.right = self._insert(data, node.right)
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance_factor = self.get_balance(node)
        
        if balance_factor > 1 and data < node.left.data:
            return self.rotate_right(node)
        if balance_factor < -1 and data > node.right.data:
            return self.rotate_left(node)
        if balance_factor > 1 and data > node.left.data:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance_factor < -1 and data < node.right.data:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node

    def delete(self, data):
        if self.root:
            self.root = self._delete(data, self.root)

    def _delete(self, data, node):
        if not node:
            return node
        elif data < node.data:
            node.left = self._delete(data, node.left)
        elif data > node.data:
            node.right = self._delete(data, node.right)
        else:
            if not node.left and not node.right:
                node = None
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else:
                min_node = self._find_min_node(node.right)
                node.data = min_node.data
                node.right = self._delete(min_node.data, node.right)
        
        if not node:
            return node
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance_factor = self.get_balance(node)
        
        if balance_factor > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance_factor < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        if balance_factor > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance_factor < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node

    def _find_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

       
