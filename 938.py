# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def getVal(val):
            return val if low <= val <= high else 0

        def dfs(node):
            if not node:
                return 0

            return getVal(node.val) + dfs(node.left) + dfs(node.right) 

        return dfs(root)
            