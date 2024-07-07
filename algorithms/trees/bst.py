class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST():
    def inorder(node):
        if node:
            BST.inorder(node.left)
            print(node.val)
            BST.inorder(node.right)
            
    def find_successor(node):
        current = node
        
        while current.left is not None:
            current = current.left
            
        return current
            
    def search(node, val):
        if not node:
            print(f'Value {val} not found')
            return False
            
        if node.val == val:
            print(f'Value {val} found')
            return True
            
        if node.val < val:
            return BST.search(node.right, val)
            
        else:
            return BST.search(node.left, val)
            
    def insert(node, val):
        if not node:
            return TreeNode(val)
            
        if node.val > val:
            node.left = BST.insert(node.left, val)
        elif node.val < val:
            node.right = BST.insert(node.right, val)
            
        return node
        
    def delete_node(root, val):
        if not root:
            return root
            
        if val < root.val:
            root.left = BST.delete_node(root.left, val)
        elif val > root.val:
            root.right = BST.delete_node(root.right, val)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
                
            elif not root.right:
                temp = root.left
                root = None
                return temp
            else:
                min_node = BST.find_successor(root.right)
                root.key = min_node.key
                root.right = BST.delete_node(root.right, min_node.key)
                
        return root
        
root = None
root = BST.insert(root, 8)
root = BST.insert(root, 3)
root = BST.insert(root, 1)
root = BST.insert(root, 6)
root = BST.insert(root, 7)
root = BST.insert(root, 10)
root = BST.insert(root, 14)
root = BST.insert(root, 4)

print("\nInorder traversal: ", end=' ')
BST.inorder(root)

print("\nIs 10 there?")
BST.search(root, 10)

print("\nDelete 10")
root = BST.delete_node(root, 10)

print("\nInorder traversal: ", end=' ')
BST.inorder(root)

print("\nIs 10 there?")
BST.search(root, 10)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
