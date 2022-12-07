from datetime import date

class Person:
    def __init__(self,imie,wiek):
        self.imie = imie
        self.wiek = wiek

    @classmethod
    def ile_od_narodzin(cls,imie,rok):
        return cls(imie,date.today().year - rok)

    @staticmethod
    def czydorosly(wiek):
        return wiek >=18


pr1 = Person('Roman',17)
print(pr1.czydorosly(pr1.wiek))
Marta = Person.czydorosly(45)
print(Marta)

print(pr1.ile_od_narodzin('Anna',1982))
pr2 = Person.ile_od_narodzin('Anna',1982)
print(pr2.wiek)
print(pr1.wiek)
