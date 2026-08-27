# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]

        while stack:
            elem = stack.pop()
            elem.left, elem.right = elem.right, elem.left
            if elem.left:
                stack.append(elem.left)
            if elem.right:
                stack.append(elem.right)
        
        return root