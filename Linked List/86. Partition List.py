# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def partition(self, head: ListNode, x: int) -> ListNode:
		if head==None or head.next==None:
			return head
		dummy1=l1=ListNode(0)
		dummy2=l2=ListNode(0)
		while head:
			if head.val<x:
				l1.next=head
				l1=l1.next
			else:
				l2.next=head
				l2=l2.next
			head=head.next
		l2.next=None
		l1.next=dummy2.next
		return dummy1.next
