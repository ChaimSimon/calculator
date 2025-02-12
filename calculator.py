from abc import ABC,abstractmethod

class calculator(ABC):
    @abstractmethod

    def add(a,b):
        pass
        
    def sub(a,b):
        pass
    
    def mul(a,b):
        x = int(input("enter a number"))
        y = int(input("enter a number"))
        c = 0
        for i in range(y):
            c += x
        return c
        
    def div(a,b):
        x = int(input("enter a number"))
        y = int(input("enter a number"))
        c = x
        d = 0
        while c:
            c -= y
            d += 1
        return d
        
    def pow(a,b):
        pass
        
    def root(a,b):
        pass
        
    
        
        
          
    
