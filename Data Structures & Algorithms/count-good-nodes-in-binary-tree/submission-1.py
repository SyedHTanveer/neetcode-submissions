# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, currMaxSoFar):
            if not node:
                return 0
            
            count = 0

            if node.val >= currMaxSoFar:
                count += 1
            
            left, right = dfs(node.left, max(currMaxSoFar,node.val)), dfs(node.right, max(currMaxSoFar, node.val))
            return count + left + right
        return dfs(root, root.val)