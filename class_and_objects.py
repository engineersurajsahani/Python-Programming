class Employee:
    
    def __init__(self):
        self.id=None 
        self.name=None 
        self.department=None 
        self.role=None
    
    def setId(self,id):
        self.id=id 
    
    def setName(self,name):
        self.name=name
        
    def setDepartment(self,department):
        self.department=department
    
    def setRole(self,role):
        self.role=role
    
    def getId(self):
        return self.id 
    
    def getName(self):
        return self.name 
    
    def getDepartment(self):
        return self.department 
    
    def getRole(self):
        return self.department 
        
e1=Employee()
e1.setId(1)
e1.setName("Suraj Sahani")
e1.setDepartment("Development")
e1.setRole("Web Developer")

e2=Employee()
e2.setId(2)
e2.setName("Amit Sahani")
e2.setDepartment("Development")
e2.setRole("Frontend Developer")

e3=Employee()
e3.setId(3)
e3.setName("Rakesh Sahani")
e3.setDepartment("Development")
e3.setRole("Backend Developer")

print("ID :- ",e1.id)
print("Name :- ",e1.name)
print("Department :- ",e1.department)
print("Role :- ",e1.role)
print("**********")
print("ID :- ",e2.id)
print("Name :- ",e2.name)
print("Department :- ",e2.department)
print("Role :- ",e2.role)
print("**********")
print("ID :- ",e3.id)
print("Name :- ",e3.name)
print("Department :- ",e3.department)
print("Role :- ",e3.role)

