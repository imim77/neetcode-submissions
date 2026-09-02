# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            arr = []
            duljina = len(q)
            for i in range(duljina):
                elem = q.popleft()
                if elem:
                    arr.append(elem.val)
                    q.append(elem.left)
                    q.append(elem.right)
            if arr:
                res.append(arr[len(arr)-1])

        return res