from collections import namedtuple

Student = namedtuple('Student',['imie','wiek','nralb'])

s = Student('Roman',21,345345)
print(f'wiek studenta: {s[1]} lat')
print(f'imię studenta: {s.imie}')
print(f"nr albumu: {getattr(s,'nralb')}")
