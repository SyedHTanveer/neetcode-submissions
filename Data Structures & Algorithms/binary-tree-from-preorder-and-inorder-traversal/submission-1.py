# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # if not preorder: return None
        
        # head = TreeNode(preorder[0])
        # left_in, right_in = [], []
        # left_pre, right_pre = [], []

        # for i in range(len(inorder)):
        #     if head.val == inorder[i]:
        #         left_in = inorder[0:i]
        #         right_in = inorder[i + 1:]
        #         left_pre = preorder[1 : 1 + len(left_in)]    # add this
        #         right_pre = preorder[1 + len(left_in):]       # add this
        
        # head.left  = self.buildTree(left_pre, left_in)
        # head.right = self.buildTree(right_pre, right_in)

        # return head

        inorder_map = {val: i for i, val in enumerate(inorder)}

        self.pre_idx = 0

        def dfs(left, right):
            if left > right: return None

            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1

            mid = inorder_map[root.val]
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)