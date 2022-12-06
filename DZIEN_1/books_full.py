class Book:
    def __init__(self,id,tytul,autor,cena=30):
        self.cena = cena
        self.autor = autor
        self.tytul = tytul
        self.idbook = id
        self.oprawa = "miękka"
        self.create_book()

    def create_book(self):
        print("nowa książka zostałą utworzona")

    def opis_book(self):
        print(f'książka {self.tytul}, autor:{self.autor}, cena: {self.cena} zł, '
              f'okładka: {self.oprawa}')

    def rabat(self):
        return 0.1*self.cena

    #getter i setters
    def get_cena(self):
        return self.cena

    def set_cena(self,nowacena):
        self.cena = nowacena

print("________________ książka _____________________")
b = Book(8,"Wiedźmin","Andrzej Sapkowski",38)
b.oprawa = "twarda"
b.opis_book()
print(f'standardowy rabat: {b.rabat():.2f} zł')
print(f"przecena ->")
b.set_cena(36.6)
print(f"nowa cena: {b.get_cena():.2f} zł")
print(f'nowy rabat: {b.rabat():.2f} zł')
print(f'do zapłaty: {b.get_cena() - b.rabat():.2f} zł')

print("________________ książka _____________________")

db = Book(13,"Hobbit","J.R.R Tolkien",41)
db.opis_book()
print(f'standardowy rabat: {db.rabat():.2f} zł')
print(f'do zapłaty: {db.get_cena() - db.rabat():.2f} zł')
