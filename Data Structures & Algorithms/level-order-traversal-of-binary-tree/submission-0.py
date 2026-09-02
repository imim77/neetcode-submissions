# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            br_elemenata = len(q)
            level = []
            for i in range(br_elemenata):
                elem = q.popleft()
                if elem:
                    level.append(elem.val)
                    q.append(elem.left)
                    q.append(elem.right)
            if level:
                res.append(level)
        return res