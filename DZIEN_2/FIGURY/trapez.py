from figura import Figura

class Trapez(Figura):
    def __init__(self,a,b,h):
        super().__init__(a,b)
        self.h = h

    def policzpole(self):
        return (self.a+self.b)*self.h/2
    
