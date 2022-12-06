
print("***** przypadek 1 *********")
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

print("***** przypadek 2 *********")
class KwadratLiczby(int):
    def __new__(cls, wart):
        return super().__new__(cls,wart**2)

wx = KwadratLiczby(4)
print(wx)


print("***** przypadek 3 *********")
class Pacjent:
    def __new__(cls, imie,nazwisko):
        obj = super().__new__(cls)

        obj.imie = imie
        obj.nazwisko = nazwisko

        obj.pelne_dane = f'{imie} {nazwisko}'
        return obj

pc = Pacjent('Jan','Kowalski')
print(pc.pelne_dane)
print(pc.__dict__)

