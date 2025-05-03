#Tags: Easy, Linked_Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        st=set()

        curA=headA
        curB=headB
        while curA!=None:
            st.add(curA)
            curA=curA.next
        while curB!=None:
            if curB in st:
                return curB
            curB=curB.next
        return None