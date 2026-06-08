# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #DFS solution
        #we go as far left as we can
        #we track everything on our way back up
        arr = []
        res = -1
        def dfs(node):
            if not node:
                return

            #inorder traversal will automatically sort the array in a binary search tree
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        
        return arr[k-1]
