from abc import ABC,abstractmethod

class AbstractProductA(ABC):
    
    @abstractmethod
    def useful_function(self)->str:
        pass
    
