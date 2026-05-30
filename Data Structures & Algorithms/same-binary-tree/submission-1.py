# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #we check if theyre both null
        if p is None and q is None:
            return True
        #if only one is null it is false
        if not p or not q:
            return False
        # check the roots and the children
        return (p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))