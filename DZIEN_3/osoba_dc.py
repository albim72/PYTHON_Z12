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
