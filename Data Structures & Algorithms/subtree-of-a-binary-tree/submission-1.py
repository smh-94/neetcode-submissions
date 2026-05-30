# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if root doesn't exist just return false
        if not root:
            return False
        #check we're already at the similar roots
        if self.isSameTree(root, subRoot):
            return True
        #if not then we check the children
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self,root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if not root or not subRoot:
            return False
        return (root.val == subRoot.val and self.isSameTree(root.left,subRoot.left) and self.isSameTree(root.right,subRoot.right))