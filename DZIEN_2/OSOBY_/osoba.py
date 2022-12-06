class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        self.pracownik = False
        self.info()

    def info(self):
        print("utworzono nową osobę...")

    def print_osoba(self):
        print(f'osoba -> imię: {self.imie}, wiek: {self.wiek}, waga: {self.waga} kg, '
              f'wzrost: {self.wzrost} cm, kolor oczu: {self.kolor_oczu}')

    def wiek_za_x_lat(self,x):
        return self.wiek + x

    def czypracownik(self):
        return self.pracownik
