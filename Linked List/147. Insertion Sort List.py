# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def insertionSortList(self, head: ListNode) -> ListNode:
		dummy=ListNode(-1)
		dummy.next=head
		p=dummy
		while(p.next and p.next.next):
			if p.next.val<=p.next.next.val:
				p=p.next
			else:
				cur=p.next.next
				p.next.next=cur.next
				tem=dummy
				while tem.next.val<=cur.val:
					tem=tem.next
				cur.next=tem.next
				tem.next=cur
		return dummy.next
