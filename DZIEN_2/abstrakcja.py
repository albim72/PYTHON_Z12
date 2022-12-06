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
        return math.sqrt(self.x**2 + self.y**2)


class Points(APiont):
    def __init__(self,x,y,dx,dy):
        super().__init__(x,y)
        self.dx = dx
        self.dy = dy

    def point(self):
        return f'x= {self.x}, y = {self.y}'

    def distance(self):
        return super().distance() + abs((self.x-self.dx)+(self.y-self.dy))


pt = Points(4,5,1,2)
print(f'punkt: {pt.point()}')
print(f'wartość wektora przesunięcia: {pt.distance()}')
pt.info()

class MojaA(ABC):
    pass

class MojaB(ABC):
    pass

class Dwie(MojaA,MojaB):
    pass
