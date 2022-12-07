odp = input("Czy Ziemia jest płaska? Chcesz znać odpowiedź? (t/n)")
if odp.lower() == "t":
    required = True
else:
    required = False

def odpowiedz(self,*args):
    print("Tak! Ziemia jest płaska!")

def odpowiedz_new(self,*args):
    print("Nie! Ziemia jest elipsoidą!")

def brak(self):
    print("brak odpowiedzi.")

class SednoOdpowiedzi(type):
    def __init__(cls,clsname,basics,attrs):
        if required:
            if clsname == 'Kopernik':
                cls.odpowiedz = odpowiedz_new
            else:
                cls.odpowiedz = odpowiedz
        else:
            cls.odpowiedz = brak


class Arystoteles(metaclass=SednoOdpowiedzi):
    pass
class Platon(metaclass=SednoOdpowiedzi):
    pass
class SwTomasz(metaclass=SednoOdpowiedzi):
    pass
class Kopernik(metaclass=SednoOdpowiedzi):
    pass


ary = Arystoteles()
print(f'Filozof -> {ary.__class__.__name__} :' ,end="")
ary.odpowiedz()

pla = Platon()
print(f'Filozof -> {pla.__class__.__name__} :' ,end="")
pla.odpowiedz()

swt = SwTomasz()
print(f'Filozof -> {swt.__class__.__name__} :' ,end="")
swt.odpowiedz()

kop = Kopernik()
print(f'Filozof -> {kop.__class__.__name__} :' ,end="")
kop.odpowiedz()


