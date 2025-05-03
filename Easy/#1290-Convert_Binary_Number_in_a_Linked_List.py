#Tags: Easy, Linked_Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        res=0
        cur=head
        while cur:
            res= (res*2) + cur.val
            cur=cur.next
        return res