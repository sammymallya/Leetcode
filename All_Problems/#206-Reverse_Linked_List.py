#Tags: Easy
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        cur=head
        prev=None
        nxt=head.next

        cur.next=prev
        while nxt:
            prev=cur
            cur=nxt
            nxt=cur.next
            cur.next=prev
        return cur