# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(node,maxNode):
            nonlocal count
            if not node:
                return None
            if node.val>=maxNode:
                count+=1
            maxNode=max(node.val,maxNode)
            dfs(node.left,maxNode)
            dfs(node.right,maxNode)
        dfs(root,root.val)
        return count
        
        