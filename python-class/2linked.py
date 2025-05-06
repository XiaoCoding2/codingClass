
class Node:
    def __init__(self,val):
        self.val :Node|None = val
        self.next:Node|None = None
        self.prev:Node|None = None

class doublyll:
    def __init__(self):
        self.head:Node|None = None
    #
    def addend(self,data):
        newnode=Node(data) #creates new node
        if not self.head: #if head is empty
            self.head=newnode
            print("added to linked list")
            return
        current=self.head
        while current.next: #while next val is not none
            current=current.next
        current.next=newnode
        newnode.prev=current
        print("Added to linked list")
    #
    def addbeg(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    #
    def printfor(self):
        if not self.head:
            print("None")
            return
        cur=self.head
        while cur.next:               
            print(cur.val,end=" -> ")
            cur=cur.next              
        print(cur.val,end=" -> ")    
        print("None")
    #
    def printback(self):
        if not self.head:
            print("None")
            return
        cur=self.head
        while cur.next: 
            cur=cur.next
        while cur.prev:
            print(cur.val,end=" <- ")
            cur=cur.prev
        print(cur.val,end=" <- ")
        print("None")
    #
    def deletekey(self,item):
        current=self.head
        if current.val==item and current:
            self.head=current.next
        while current.next:
            current=current.next
            if current.val==item:
                current.prev.next=current.next
                current.next.prev=current.prev
                return
    #
    def rotate(self):
        if not self.head:
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.val,self.head.val=self.head.val,cur.val
        print(cur.val)
    #
    def tailatbeg(self):
        if not self.head:
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.prev.next=None
        self.addbeg(cur.val)

dll=doublyll()
dll.addend("b")
dll.addend("c")
dll.addend("d")
dll.addbeg("a")

dll.printfor()
dll.printback()

dll.tailatbeg()

dll.printfor()
