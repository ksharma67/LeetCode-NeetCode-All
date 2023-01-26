# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        dummy = pre = ListNode(0, head)
        for _ in range(left - 1):
            pre = pre.next
        new_pre = None
        current = pre.next
        for _ in range(right - left + 1):
            tmp = current.next
            current.next = new_pre
            new_pre = current
            current = tmp
        pre.next.next = current
        pre.next = new_pre
        return dummy.next
