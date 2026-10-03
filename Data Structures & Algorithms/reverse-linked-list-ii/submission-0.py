# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        leftN=head
        dummy=ListNode(0,head)
        L=dummy
        for i in range(left-1):
            leftN=leftN.next
            # dummy=dummy.next
            L=L.next
        rightN=leftN
        for i in range(right-left):
            rightN=rightN.next
        
        R=rightN.next
        prev=R
        cur=leftN
        for i in range(right-left+1):
            Nxt=cur.next
            cur.next=prev
            prev=cur
            cur=Nxt
        L.next=prev

        return dummy.next




        
        

        