from osoba import Osoba
from pracownik import Pracownik

za = 12
print("________________ osoba ______________")
os1 = Osoba("Jan",44,98,175)
os1.print_osoba()
print(f'wiek za {za} lat wynosi: {os1.wiek_za_x_lat(za)}')
print(f'czy osoba jest pracownikiem? ({os1.czypracownik()})')

print("________________ osoba ______________")
os2 = Osoba("Olga",23,51,163)
os2.print_osoba()
print(f'wiek za {za} lat wynosi: {os2.wiek_za_x_lat(za)}')
print(f'czy osoba jest pracownikiem? ({os2.czypracownik()})')

print("_____________pracownik_____________")
pr1 = Pracownik("Karol",54,102,175,"ABC","dyrektor",12,10340)
pr1.print_osoba()
pr1.print_pracownik()
print(f'wiek za {za} lat wynosi: {pr1.wiek_za_x_lat(za)}')
print(f'czy osoba jest pracownikiem? ({pr1.czypracownik()})')
