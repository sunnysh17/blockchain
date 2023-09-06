class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
               if self.right is None:
                  self.right = Node(data)
               else:
                  self.right.insert(data)
      else:
         self.data = data
      
      
   # Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res
   
   def preorderTraversal(self,root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.preorderTraversal(root.left)
         res = res + self.preorderTraversal(root.right)
      return res
   
   def postorderTraversal(self,root):
      res = []
      if root:
         res = res + self.postorderTraversal(root.left)
         res = res + self.preorderTraversal(root.right)
         res.append(root.data)
      return res

   
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print("Inorder: ",root.inorderTraversal(root))
print("Preorder", root.preorderTraversal(root))
print("Postorder", root.postorderTraversal(root))

