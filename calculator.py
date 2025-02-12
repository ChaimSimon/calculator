from abc import ABC,abstractmethod

class calculator(ABC):
    @abstractmethod

    def add(self,a,b):
        return a + b
        
    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        pass
    
    def mul(a,b):
        x = int(input("enter a number"))
        y = int(input("enter a number"))
        c = 0
        for i in range(y):
            c += x
        return c
        
    def pow(self,a,b):
        pass
    def div(a,b):
        x = int(input("enter a number"))
        y = int(input("enter a number"))
        c = x
        d = 0
        while c:
            c -= y
            d += 1
        return d

    def root(self,a,b):
        pass
        
    
        
        
          
    
