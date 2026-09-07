# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = [] 
        q = deque()
        q.append(root)
  
        
        while q:
            qLen = len(q) 
            for i in range(qLen):
                elem = q.popleft()
                if elem:
                    res.append(str(elem.val))
                    q.append(elem.left)
                    q.append(elem.right)
                else:
                    res.append(str(None))

        return ",".join(res) 

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "None":
            return None

        root = TreeNode(int(vals[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()

            if vals[index] != "None":
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
            index += 1
            
            if vals[index] != "None":
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index += 1

        return root