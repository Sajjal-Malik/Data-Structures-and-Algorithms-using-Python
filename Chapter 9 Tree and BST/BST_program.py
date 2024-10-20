class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    # inserting data using recursion
    def insert(self, data):
        self.root = self.recursive_insert(self.root, data)

    def recursive_insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.recursive_insert(root.left, data)
        elif data > root.item:
            root.right = self.recursive_insert(root.right, data)
        return root

    # searching data using recursion
    def search(self, data):
        return self.recursive_search(self.root, data)
    
    def recursive_search(self,root, data):
        if root == None or root.item == data:
            return root
        if data < root.item:
            return self.recursive_search(root.left, data)
        else:
            return self.recursive_search(root.right, data)
    
    # inorder traversal using recursive
    def inorder(self):
        result = []
        self.recursive_inorder(self.root, result)
        return result
    
    def recursive_inorder(self,root,result):
        if root:
            self.recursive_inorder(root.left, result)
            result.append(root.item)
            self.recursive_inorder(root.right, result)
    
    # preorder traversal using recursive
    def preorder(self):
        result = []
        self.recursive_preorder(self.root, result)
        return result
    
    def recursive_preorder(self,root,result):
        if root:
            result.append(root.item)
            self.recursive_preorder(root.left, result)
            self.recursive_preorder(root.right, result)
    
    # postorder traversal using recursive
    def postorder(self):
        result = []
        self.recursive_postorder(self.root, result)
        return result
    
    def recursive_postorder(self,root,result):
        if root:
            self.recursive_postorder(root.left, result)
            self.recursive_postorder(root.right, result)
            result.append(root.item)

    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item
    
    def max_value(self,temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item

    def delete(self, data):
        self.root = self.recursive_delete(self.root, data)
        return self.root

    def recursive_delete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.recursive_delete(root.left, data)
        elif data > root.item:
            root.right = self.recursive_delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)
            self.recursive_delete(root.right, root.item)
        return root

    def size(self):
        return len(self.postorder())
