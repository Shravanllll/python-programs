class Geek:
      
    
     def __init__(self, name, age):
           
           self.geekName = name
           self.geekAge = age
 
        
     def displayAge(self):
           
          
           print("Age: ", self.geekAge)
 

obj = Geek("R2J", 20)
 

print("Name: ", obj.geekName)
 

obj.displayAge()
