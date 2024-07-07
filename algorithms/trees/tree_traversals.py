class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeTraversals:
    def inorder(node):
        if node:
            TreeTraversals.inorder(node.left)
            print(node.val)
            TreeTraversals.inorder(node.right)
            
    def preorder(node):
        if node:
            print(node.val)
            TreeTraversals.preorder(node.left)
            TreeTraversals.preorder(node.right)
            
    def postorder(node):
        if node:
            TreeTraversals.postorder(node.left)
            TreeTraversals.postorder(node.right)
            print(node.val)
            
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder traversal ")
TreeTraversals.inorder(root)

print("\nPreorder traversal ")
TreeTraversals.preorder(root)

print("\nPostorder traversal ")
TreeTraversals.postorder(root)
