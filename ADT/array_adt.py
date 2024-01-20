# Array ADT 

class ArrayADT:
    
    def __init__(self,size):
        self.l=[None]*size
        
    def insert(self,index,data):
        self.l[index]=data
        
    def update(self,index,data):
        self.l[index]=data 
        
    def delete(self,index):
        del self.l[index]
        
    def printArray(self):
        print(self.l)
        
a=ArrayADT(10)

a.printArray()

a.insert(0,11)
a.insert(1,22)
a.insert(2,33)

a.printArray()

a.update(2,44)

a.printArray()

a.delete(2)

a.printArray()
