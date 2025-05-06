
class Stack:
    def __init__(self):
        self.items=[]
    #
    def push(self, item):
        self.items.append(item)
    #
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
    #
    def is_empty(self):
        return len(self.items)==0
    #
    def size(self):
        len(self.items)
    #
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")
    #
    def reverse(self,s):
        stack=Stack()
        r_str=""
        for lttr in s:
            self.push(lttr)
        while not self.is_empty():
            r_str+=self.peek()
            self.pop()
        return r_str

s=Stack()

in_str="Hello"
r=s.reverse(in_str)
print(r)