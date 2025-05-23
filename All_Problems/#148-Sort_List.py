class ll:
    def __init__ (self):
        self.head=None
class node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

li=ll()
head=node(4)
n2=node(1)
n3=node(2)
n4=node(4)

li.head=head
head.next=n2
n2.next=n3
n3.next=n4

cur=head
while cur:
    print(cur.val)
    cur=cur.next
