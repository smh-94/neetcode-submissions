# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #empty list
        if not root:
            return []
        res = []
        #we use a deque bc we need to pop from left and append to right
        #deque call
        q = collections.deque()
        # start the loop with root in the deque
        q.append(root)

        while q:
            #take current length of the q
            qLen = len(q)
            level = []
            for i in range(qLen):
                #pop node
                node = q.popleft()
                if node:
                    # add to current level
                    level.append(node.val)
                    # add next level's nodes to queue
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res