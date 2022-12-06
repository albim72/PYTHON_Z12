from prostokat import  Prostokat
from trojkat import Trojkat
from trapez import Trapez
from kolo import Kolo

pr = Prostokat(5.5,7.8)
print(f'Pole figury: {pr.__class__.__name__} wynosi: {pr.policzpole():.2f} cm2')

tr = Trojkat(5.5,8.9)
print(f'Pole figury: {tr.__class__.__name__} wynosi: {tr.policzpole():.2f} cm2')

trp = Trapez(6.3,4.8,4.1)
print(f'Pole figury: {trp.__class__.__name__} wynosi: {trp.policzpole():.2f} cm2')

#stwórz klasę Kolo(Figura) i policz pole koła dla promienia 5.5
kl = Kolo(5.5)
print(f'Pole figury: {kl.__class__.__name__} wynosi: {kl.policzpole():.2f} cm2')
