#Tags: Medium, Linked_Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None or k==0:
            return head
        #finding length of list:
        tail=head
        length=1
        while tail.next:
            length+=1
            tail=tail.next
        #normalizing k
        k=k%length

        #making list circular
        tail.next=head

        #moving k steps forward
        new_tail=head
        for _ in range(length-k-1):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        return new_head