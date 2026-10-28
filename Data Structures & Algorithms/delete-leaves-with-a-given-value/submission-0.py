# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root,prev):
            if not root:
                return
            
            #如果说这个节点是叶子呢,要记录一下prev吗？
            dfs(root.left,root)
            dfs(root.right,root)
            if not root.left and not root.right and root.val==target:
                #那就要把root给删掉
                if prev.left==root:
                    prev.left=None
                else:
                    prev.right=None
                
        prev=TreeNode(0)
        prev.left=root
        dfs(root,prev)
        return prev.left
        