# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []

        def dfs(node, inorder):
            if not root:
                return None

            if node.left:dfs(node.left, inorder)
            inorder.append(node.val)
            if node.right: dfs(node.right, inorder)
        dfs(root, inorder)

        return inorder