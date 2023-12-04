# Define binary tree Node
class Node:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def invertTree(self, root: Node) -> Node:
    if root == None:
      return None
    root.left, root.right = self.invertTree(root.right),self.invertTree(root.left)
    return root
    
