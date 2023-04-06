class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    if val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def delete(root, val):
    if not root:
        return None
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        temp = root.right
        while temp.left:
            temp = temp.left
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root


# Criando a raiz
root = TreeNode(5)

# Inserindo alguns valores
insert(root, 3)
insert(root, 8)
insert(root, 2)
insert(root, 4)
insert(root, 7)
insert(root, 9)

# Buscando por um valor
node = search(root, 4)
if node:
    print("Valor encontrado:", node.val)
else:
    print("Valor não encontrado")

# Removendo um nó
root = delete(root, 8)
node = search(root, 8)
if node:
    print("Valor encontrado:", node.val)
else:
    print("Valor não encontrado")

