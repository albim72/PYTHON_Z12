from dataclasses import dataclass,Field
from datetime import datetime

@dataclass
class Person:
    name:str
    surname:str
    year_birth:int

    @property
    def age(self):
        return datetime.now().year  - self.year_birth


p1 = Person('Janusz','Kot',1975)
print(p1)

print(p1.age)

#inne spojrzenie....
#Field -> ('default','default_factory','init','repr','hash','compare','metadata','kw_only')

params = {
    'name':Field(None,None,True,True,True,True,None,None),
    'surname':Field(None,None,True,True,True,True,None,None),
    'year_birth':Field(None,None,True,True,True,True,None,None)

}

def age(self):
    return datetime.now().year - self.year_birth
#metadefinicja klasy
Person = dataclass(type('Person',(),{'__annotations__':params,'age':property(age)}))

pr = Person('Romulada','Tracz',1965)
print(pr)
print(pr.age)
