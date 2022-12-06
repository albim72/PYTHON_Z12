from osoba import Osoba
from pracownik import Pracownik
from student import Student

za = 12
print("________________ osoba 1______________")
os1 = Osoba("Jan",44,98,175)
os1.print_osoba()
print(f'wiek za {za} lat wynosi: {os1.wiek_za_x_lat(za)}')
print(f'czy osoba jest pracownikiem? ({os1.czypracownik()})')

print("________________ osoba 2______________")
os2 = Osoba("Olga",23,51,163)
os2.print_osoba()
print(f'wiek za {za} lat wynosi: {os2.wiek_za_x_lat(za)}')
print(f'czy osoba jest pracownikiem? ({os2.czypracownik()})')

print("_____________pracownik 1_____________")
pr1 = Pracownik("Karol",54,102,175,"ABC","dyrektor",12,10340)
pr1.print_osoba()
pr1.print_pracownik()
print(f'wiek za {za} lat wynosi: {pr1.wiek_za_x_lat(za)}')
print(f'czy osoba jest pracownikiem? ({pr1.czypracownik()})')

print("_____________student 1_____________")
st1 = Student("Olaf",22,80,178,53453,"budowlany","budowa mostów",3)
st1.print_osoba()
st1.print_student()
print(f'wiek za {za} lat wynosi: {st1.wiek_za_x_lat(za)}')
print(f'czy osoba jest pracownikiem? ({st1.czypracownik()})')

print("_____________student 2_____________")
st2 = Student("Paula",23,58,174,7756756,"ekonomia","ekonomika",4,"XYZ","sekretarka",1,2500)
st2.print_osoba()
st2.print_student()
st2.print_pracownik()
print(f'wiek za {za} lat wynosi: {st2.wiek_za_x_lat(za)}')
print(f'czy osoba jest pracownikiem? ({st2.czypracownik()})')

print("_____________student 3_____________")
st3 = Student("Robert",22,72,177,6345414,"informatyka i automatyka","informatyka",3,dyscyplina="biegi ultra",lata_upr=4,
              zyciowka="84km 11h 34min 5s")
st3.print_osoba()
st3.print_student()
print(st3.infosport())
print(f'wiek za {za} lat wynosi: {st3.wiek_za_x_lat(za)}')
print(f'czy osoba jest pracownikiem? ({st3.czypracownik()})')
