class A:
    
    def display(slef):
        print("Class A")
    
class B(A):
    
    def display(slef):
        print("Class B")

class C(A):
    
    def display(slef):
        print("Class C")
        
class D(B,C):
    
    def display(slef):
        print("Class D")
        
a=A()
a.display()

b=B()
b.display()

c=C()
c.display()

d=D()
d.display()
    
