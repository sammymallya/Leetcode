#Tags:  Medium, Linked_Lists, Two_Pointer
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        slow=dummy
        fast=dummy
        for i in range(n+1):
            if fast:
                fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        if slow and slow.next:
            slow.next=slow.next.next
        return dummy.next
