# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        #其实就是写了一个dfs
        cache={None:0}
        def dfs(root):
            if root in cache:
                return cache[root]
            cache[root]=root.val#如果选择当前节点
            #那就要跳过孩子
            if root.left:
                cache[root] += dfs(root.left.left)+dfs(root.left.right)
            if root.right:
                cache[root] += dfs(root.right.left)+dfs(root.right.right)
            cache[root]=max(cache[root],dfs(root.left)+dfs(root.right))
            return cache[root]
        return dfs(root)

        

