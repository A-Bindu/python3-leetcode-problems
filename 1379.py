class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q=[]
        q.append(cloned)
        while q:
            a=q.pop(0)
            if a.val==target.val:
                return a
            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)