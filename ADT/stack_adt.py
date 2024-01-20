# Stack ADT 

class StackADT:
    
    def __init__(self):
        self.l=[]
        
    def push(self,data):
        self.l.append(data)
        
    def pop(self):
        del self.l[-1]
        
    def peek(self):
        print(self.l[-1])
        
    def isEmpty(self):
        return len(self.l)==0
    
    def size(self):
        print(len(self.l))
        
s=StackADT()

s.push(11)
s.push(22)
s.push(33)
s.push(44)
s.push(55)

s.peek()

s.pop()

s.peek()

print(s.isEmpty())

s.size()
