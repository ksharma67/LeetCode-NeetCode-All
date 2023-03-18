# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp,c=head,0
        while temp:
            c+=1
            temp=temp.next
        temp,n=head,c//2
        a=[]
        while n!=0:
            a.append(temp.val)
            temp=temp.next
            n-=1
        n,m=c//2-1,0
        while temp:
            m=max(temp.val+a[n],m)
            temp=temp.next
            n-=1
        return m
