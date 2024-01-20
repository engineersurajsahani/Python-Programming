# Set ADT 

class SetADT:
    
    def __init__(self):
        self.l=[]
        
    def insert(self,data):
        if data in self.l:
            print(data," is already present in the set !!!")
        else:
            self.l.append(data)
        
    def delete(self,data):
        if data in self.l :
            self.l.remove(data)
        else:
            print(data," is not present in the set !!!")
            
    def contains(self,data):
        if data in self.l :
            print(data," is  present in the set !!!")
        else:
            print(data," is not present in the set !!!")
            
    def isEmpty(self):
        if len(self.l)==0:
            print("Set is Empty !!!")
        else:
            print("Set is not empty")
            
    def size(self):
        print(len(self.l))
        
    def printSet(self):
        print(self.l)
        
s=SetADT()

s.insert(11)
s.insert(22)
s.insert(11)
s.insert(33)
s.insert(22)

s.printSet()

s.delete(33)

s.printSet()

s.contains(100)

s.isEmpty()

s.size()


        
    
