class IntFloatValueError(Exception):
    def __init__(self,value):
        self.value = value
        
    def __str__(self):
        return f'wartość {self.value} jest niewłaściwa, ' \
               f'klasa CustomIntFloatDict akceptuje tylko wartości int i float'
