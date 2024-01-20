# Queue ADT

class QueueADT:
    
    def __init__(self):
        self.l=[]
        
    def enqueue(self,data):
        self.l.append(data)
        
    def dequeue(self):
        del self.l[0]
        
    def peek(self):
        print(self.l[0])
        
    def isEmpty(self):
        return len(self.l)==0
        
    def size(self):
        print(len(self.l))
        
q=QueueADT()

q.enqueue(11)
q.enqueue(22)
q.enqueue(33)
q.enqueue(44)
q.enqueue(55)

q.peek()

q.dequeue()

q.peek()

print(q.isEmpty())

q.size()
