from dataclasses import dataclass

@dataclass
class Article:
    title:str
    content:str
    author:str


@dataclass(init=False)
class PythonArticle(Article):
    language:str
    author:str
    price:int = 0

    def __init__(self,title,price):
        self.title = title
        self.price = price
        self.language = "Python"
        self.author = "Marcin Albiniak"
        self.content = "opis wybranych aspektów użycia jęzka Python"

    def rabat(self):
        print(f'publikacja: {self.title}, autor: {self.author}, cena: {self.price} zł, '
              f'rabat: {self.price*0.1} zł')


art = PythonArticle("Algorytmy DL",89)
print(art)
art.rabat()
