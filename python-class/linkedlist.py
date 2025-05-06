class Node:
    def __init__(self,data):
        self.data:Node|None=data
        self.next:Node|None = None

'''
Linked list, kind of like variables.
Stores the current var, and also points to anouther var
'''
from time import time
class Linkedlist:
    def __init__(self):
        self.head=None
    #
    def insertend(self,data):
        newnode=Node(data) #creates new node
        if not self.head: #if head is empty
            self.head=newnode
            #print("added to linked list")
            return
        current=self.head
        while current.next: #while next val is not none
            current=current.next
        current.next=newnode
        #print("Added to linked list")
    #
    def insertbeg(self, data):
        newnode=Node(data)
        #connect with linked list
        newnode.next=self.head
        #make it the new head
        self.head=newnode
    #
    def removenode(self, item):
        current=self.head
        if current.data==item and current:
            self.head=current.next
        prev=None
        while current.next:
            prev=current
            current=current.next
            if current.data==item:
                prev.next=current.next
                return
    #
    def findcenter(self):
        if self.head==None or self.head.next==None:
            return self.head
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
        mid=count//2
        if count%2==1:
            mid+=1
        cur=self.head
        for x in range(mid):
            if x==mid-1:
                return cur.data
            cur=cur.next
        return
    #
    def fastcenter(self):
        if self.head==None:
            return self.head.data
        cur=self.head
        dub=self.head
        while dub and dub.next:
            cur=cur.next
            dub=dub.next.next
        return cur
    #
    def search(self,a): ...
    #
    def hascycle(self)-> bool:
        if self.head==None:
            return False
        cur=self.head
        dub=self.head
        while dub and dub.next:
            cur=cur.next
            dub=dub.next.next
            if cur==dub:
                return True
        return False
    #
    def reverse(self,head):
        if head.data==None or head.next.data==None:
            return head
        lst=[]
        cur=head
        while cur.next:
            lst.append(cur.data)
            cur=cur.next
        lst.append(cur.data)
        head=cur
        #print("part1")
        #print(lst)
        cur2=head
        for i in range(len(lst)-2,0,-1):
            newnode=Node(lst[i])
            cur2.next=newnode
            cur2=cur2.next
        cur2.next=Node(lst[0])
        return head
    #
    def palindrome(self):
        center=self.fastcenter()
        point2=self.reverse(center)
        point1=self.head
        try:
            while point1!=point2:
                if point1.data!=point2.data:
                    return False
                point1=point1.next
                point2=point2.next
            return True
        except:
            return True
    #
    def nth_con_end(self,n):
        head=self.head
        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
        times=count-n
        cur=head
        for x in range(times):
            cur=cur.next
        return cur.data
    #
    def nthFromEnd(self,n):
        head=self.head
        fast=head
        slow=head
        for x in range(n):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        return slow.data
    #
    def printll(self):
        if not self.head:
            print("None")
            return
        cur=self.head
        while cur.next:               
            print(cur.data,end=" -> ")
            cur=cur.next              
        print(cur.data,end=" -> ")    
        print("None")

ll=Linkedlist()

def Norm(lst,n):
    return lst[len(lst)-n]


for x in range(10_000):
    ll.insertend(x)
#ll.insertend("a")
#ll.insertend("b")
#ll.insertend("c")
#ll.insertend("d")
#a b c d
lst=[x for x in range(10_000)]


#ll.printll()
#0.00098586082458496094
'''
start=time()
print(ll.nthFromEnd(2),"nthFromEnd")
end=time()
print(f"{end-start:.20f}")


start2=time()
print(ll.nth_con_end(2),"nth_con_end")
end2=time()
print(f"{end2-start2:.20f}")
'''

start3=time()
print(Norm(lst,2),"Norm")
end3=time()
print(f"{end3-start3:.20f}")

#ll.removenode("q")
#a b c
#ll.insertend("d")

#print(ll.fastcenter())

'''

ll.insertend(1)
ll.insertend(0)
ll.insertend(0)
ll.insertend(1)
print(ll.palindrome())
'''