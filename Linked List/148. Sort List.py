# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):           
        slow = fast = head             
        while fast and fast.next:      
            fast = fast.next.next
            if fast: slow = slow.next
        mid, slow.next = slow.next, None   
        return mid
        
    def merge(self, left, right):
        head = prev = None    
        while left and right:  
            mini = right        
            if left.val < right.val:
                mini = left
                left = left.next
            else: right = right.next
        
            if not head: head = prev = mini      
            else: prev.next = prev = mini        
        if left: prev.next = left                
        if right: prev.next = right              
        return head
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next): return head    
        mid = self.getMid(head)                     
        left = self.sortList(head)                   
        right = self.sortList(mid)                   
        return self.merge(left, right)  
