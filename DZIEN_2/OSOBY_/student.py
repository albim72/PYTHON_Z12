from pracownik import Pracownik
from sport import Sport
from ekstra import Ekstra

class Student(Pracownik,Sport,Ekstra):
    def __init__(self,imie,wiek,waga,wzrost,nr_studenta,wydzial,kierunek,rok_st,
                 firma="",stanowisko="",latapracy="",wynagrodzenie="",dyscyplina="",lata_upr="",zyciowka=""):
        Pracownik.__init__(self,imie,wiek,waga,wzrost,firma,stanowisko,latapracy,wynagrodzenie)
        Sport.__init__(self,dyscyplina,lata_upr,zyciowka)
        self.nr_studenta = nr_studenta
        self.wydzial = wydzial
        self.kierunek = kierunek
        self.rok_st = rok_st
        
    def print_student(self):
        print(f'student {self.nr_studenta}, wydział: {self.wydzial}, kierunek: {self.kierunek}, '
              f'rok studiów: {self.rok_st}')

    def czypracownik(self):
        return self.firma != ""
        
