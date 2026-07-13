# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first=head
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        curr=second
        while curr:
            nextNode=curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        second=prev
        while second:
            val1=first.next
            val2=second.next
            first.next=second
            second.next=val1
            first=val1
            second=val2

