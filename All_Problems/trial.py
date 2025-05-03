class listNode():
    def __init__ (self, data,next=None):
        self.data = data
        self.next=next

class linkedList():
    def __init__ (self):
        self.head =None
    
ll1=linkedList()        #4,1,8,4,5
ll2=linkedList()        #5,6,1,8,4,5

headA=listNode(4)
headB=listNode(5)


node2=listNode(1)
node3=listNode(8)
node4=listNode(4)
node5=listNode(5)
node6=listNode(6)
node7=listNode(1)

#connecting nodes
headA.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

headB.next=node6
node6.next=node7
node7.next=node3

#logging output
def pll(head):
    cur=head
    while cur!=None:
        print(cur.data)
        cur=cur.next
# print("Linked list A is:\n")
# pll(headA)
# print("Linked list B is: \n")
# pll(headB)               
def find_int(headA,headB):
    st=set()

    curA=headA
    while curA!=None:
        st.add(curA)
        curA=curA.next
    curB=headB

    while curB!=None:
        if curB in st:
            return curB.data
        curB=curB.next
    return None
print("Intersecting node is: ",find_int(headA,headB))