# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = k-1
        temp = head
        lens = 0
        while(i and temp.next):
            temp = temp.next
            i -= 1
            lens += 1
        
        t2 = temp

        while(t2.next):
            t2 = t2.next
            lens += 1

        togo = lens-k+1
        t3 = head 
        for i in range(togo):
            t3 = t3.next
        
        t3.val, temp.val = temp.val, t3.val 

        return head
