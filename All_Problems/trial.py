class listNode():
    def __init__ (self, data,next=None):
        self.data = data
        self.next=next

class linkedList():
    def __init__ (self):
        self.head =None
    
ll1=linkedList()        #41,2,3,4,5,5
head=listNode(1)
node2=listNode(2)
node3=listNode(4)
node4=listNode(4)
node5=listNode(5)

head.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

dummy=listNode(None)
dummy.next=head

cur=head
prev=dummy
nxt=cur.next
while cur and nxt:
    # if cur.data==4:
    #     prev.next=cur.next
    #     cur=cur.next
    # else:
    #     prev=cur
    #     cur=cur.next
    if cur.data==4:
        prev.next=nxt
        cur=cur.next
        nxt=nxt.next
    else:
        prev=cur
        cur=nxt
        nxt=cur.next

    
    

cur=head
while cur!=None:
    print(cur.data)
    cur=cur.next