class Employee:
    
    def __init__(self,id,name,department,role):
        self.id=id 
        self.name=name 
        self.department=department 
        self.role=role
    
    def __init__(self):
        pass 
    
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
    
    def geName(self):
        return self.name 
    
    def getDepartment(self):
        return self.department 
    
    def getRole(self):
        return self.role 
        
    def display(self):
        print("Id :- ",self.id," Name :- ",self.name," Department :- ",self.department," Role :- ",self.role)

e1=Employee()
e1.setId(1)
e1.setName("Suraj Sahani")
e1.setDepartment("Developer")
e1.setRole("Backend")

e2=Employee()
e2.setId(2)
e2.setName("Amit Sahani")
e2.setDepartment("Developer")
e2.setRole("Frontend")

e3=Employee()
e3.setId(3)
e3.setName("Rakesh Sahani")
e3.setDepartment("Developer")
e3.setRole("UI")

e1.display()
e2.display()
e3.display()