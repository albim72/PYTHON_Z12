class Pojazd:
    #dunder
    #double underline
    def __new__(cls, marka):
        print(f'tworzenie obiektu klasy: {cls.__name__}')
        obj = object.__new__(cls)
        return obj
    def __init__(self,name):
        print(f'inicjowanie obiektu klasy Pojazd...')
        self.name = name
        

poj = Pojazd("Landrover")
