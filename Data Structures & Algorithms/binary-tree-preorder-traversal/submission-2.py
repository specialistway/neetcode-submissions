# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #root left right
        #morris
        res=[]
        cur=root
        while cur:
            if not cur.left:#如果没有左子树 那么要进入右子树
                res.append(cur.val)#先根
                cur=cur.right
            else:#如果有左子树
                #先找到左
                prev=cur.left
                while prev.right and prev.right!=cur:
                    prev=prev.right
                if not prev.right:
                    res.append(cur.val)
                    prev.right=cur
                    cur=cur.left
                else:
                    cur=cur.right
                    prev.right=None
        return res

               


        


        