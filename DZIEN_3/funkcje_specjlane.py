class MDict(dict):
    def __missing__(self, key):
        return "klucz nie istnieje"

sl = {'Ala':56,'Jacek':45,'Olaf':46,'Ola':38}
print(sl['Ala'])
# print(sl['Heniek'])
md = MDict(sl)

print(md['Ala'])
print(md['Heniek'])

class Attribs:
    def __init__(self,bm):
        self.bm = bm

    def __getattr__(self, item):
        return f"Klasa nie posiada atrybutu: {item}"

f = Attribs("bm")
print(f.bar)
print(f.bm)


class JakFunkcja:
    def __init__(self):
        print("obiekt został utworzony")

    def __call__(self):
        print("instancja utworzona przez funkcję specjalną __call__")

er = JakFunkcja()
er()
