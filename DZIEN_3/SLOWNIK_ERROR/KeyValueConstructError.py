class KeyValueConstructError(Exception):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return f'klucze i wartości muszą być zadane w postaci krotku lub listy,\n' \
               f'klucze {self.key} są opisane kolekcją: {type(self.key)}\n,' \
               f'wartości {self.value} są opisane kolekcją: {type(self.value)}\n'
