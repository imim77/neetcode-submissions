# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxCurr = float("-inf")
        maxLeftAndRight = float("-inf")
        maxPath = float("-inf")

        def dfs(root):
            nonlocal maxPath, maxCurr, maxLeftAndRight
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            left = max(left, 0)
            right = max(right, 0)

            maxPath = max(maxPath, root.val+left+right)
            return root.val+max(left, right)

        dfs(root)
        return maxPath