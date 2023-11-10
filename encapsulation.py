class Employee:
    
    def __init__(self):
        self._id=None 
        self._name=None 
        self._department=None 
        self._role=None
    
    def setId(self,id):
        self._id=id 
    
    def setName(self,name):
        self._name=name
        
    def setDepartment(self,department):
        self._department=department
    
    def setRole(self,role):
        self._role=role
    
    def getId(self):
        return self._id 
    
    def getName(self):
        return self._name 
    
    def getDepartment(self):
        return self._department 
    
    def getRole(self):
        return self._role 
        
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

print("ID :- ",e1.getId())
print("Name :- ",e1.getName())
print("Department :- ",e1.getDepartment())
print("Role :- ",e1.getRole())
print("**********")
print("ID :- ",e2.getId())
print("Name :- ",e2.getName())
print("Department :- ",e2.getDepartment())
print("Role :- ",e2.getRole())
print("**********")
print("ID :- ",e3.getId())
print("Name :- ",e3.getName())
print("Department :- ",e3.getDepartment())
print("Role :- ",e3.getRole())

