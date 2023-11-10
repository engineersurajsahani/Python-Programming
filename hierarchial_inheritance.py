class A:
    
    def display(slef):
        print("Class A")
    
class B(A):
    
    def display(slef):
        print("Class B")

class C(A):
    
    def display(slef):
        print("Class C")
        
        
a=A()
a.display()

b=B()
b.display()

c=C()
c.display()
