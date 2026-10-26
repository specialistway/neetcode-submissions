# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#左中右
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #left root right
        res=[]
        cur=root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur=cur.right
            else:
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                if not prev.right:
                    prev.right=cur
                    cur=cur.left
                else:
                    res.append(cur.val)
                    prev.right=None
                    cur=cur.right
        return res

        


        
        
        