import math
from abc import ABC,abstractmethod

class APiont(ABC):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def info(self):
        print("to jest klasa opisująca dwolny punkt w dowolnej przestrzeni 2D")
        
    @abstractmethod
    def point(self):
        raise NotImplementedError
    
    @abstractmethod
    def distance(self):
        return math.sqrt(self.x**2 - self.y**2)
