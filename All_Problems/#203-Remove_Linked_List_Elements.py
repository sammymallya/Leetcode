#Tags: Easy, Linked_Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(None)
        dummy.next=head

        prev=dummy
        cur=head

        while cur:
            if cur.val==val:
                prev.next=cur.next
                cur=cur.next
            else:
                prev=cur
                cur=cur.next
        return dummy.next
        