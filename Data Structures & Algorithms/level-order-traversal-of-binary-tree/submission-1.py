# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs
        q=deque()
        res=[]
        q.append(root)
        while q:
            l=len(q)
            lst=[]
            for i in range(l):
                cur=q.popleft()
                if cur:
                    lst.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if lst:
                res.append(lst)
        return res




        