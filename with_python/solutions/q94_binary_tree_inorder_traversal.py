# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Trivial solution. 
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root is None:
        #     return []
        # else:
        #     return self.inorderTraversal(root = root.left) + [root.val] + self.inorderTraversal(root = root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        accumulator = []
        self.inorderTraversalWithAccumulator(root, accumulator)
        return accumulator
    
    def inorderTraversalWithAccumulator(self, root: Optional[TreeNode], accumulator: List[int]):
        if root is None:
            return
        else:
            self.inorderTraversalWithAccumulator(root=root.left, accumulator=accumulator)
            accumulator.append(root.val)
            self.inorderTraversalWithAccumulator(root=root.right, accumulator=accumulator)
