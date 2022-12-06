# import dane as dn
#import dane
from dane import nr_filii as filia ,book as ks
from kol_funkcje.bfunkcje import czytaj_liste,czytaj_slownik
from kol_klasy.cdane import CDane

print(filia)
print(ks)
print("__________ czytanie za pomocą funckji ________________")
czytaj_liste(filia)
czytaj_slownik(ks)

print("__________ czytanie za pomocą klasy ________________")
cd = CDane(filia,ks)
cd.czytaj_l()
cd.czytaj_s()
