# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #还是递归吧
        def insert(root):
            if val>root.val:
                #说明要往右走
                if not root.right:
                    root.right=TreeNode(val)
                    return
                insert(root.right)
            else:
                if not root.left:
                    root.left=TreeNode(val)
                    return
                insert(root.left)
        if not root:
            return TreeNode(val)
        insert(root)
        return root

        