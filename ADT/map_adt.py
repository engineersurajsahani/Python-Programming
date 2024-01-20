# Map ADT 

class MapADT:
    
    def __init__(self):
        self.m={}
        
    def put(self,key,value):
        self.m[key]=value
    
    def get(self,key):
        if key in self.m:
            print(self.m[key])
        else:
            print(key," is not present in the map !!!")
        
    def remove(self,key):
        if key in self.m:
            del self.m[key]
        else:
            print(key," is not present in the map !!!")
    
    def containsKey(self,key):
        if key in self.m:
            print(key," is present is the map !!!")
        else:
            print(key," is not present in the map !!!")
            
    def isEmpty(self):
        if len(self.m)==0:
            print("Map is empty !!!")
        else:
            print("Map is not empty !!!")
            
    def size(self):
        print(len(self.m))
        
m=MapADT()

m.put("Maths",88)
m.put("English",77)
m.put("Science",99)
m.put("History",80)
m.put("Goegraphy",77)

m.get("Science")

m.remove("History")

m.get("History")

m.containsKey("English")

m.isEmpty()

m.size()
