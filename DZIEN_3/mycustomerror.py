class MyCustomError(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None 
            
    def __str__(self):
        print("wywołanie funkcji __str__")
        if self.message:
            return f'klasa {self.__class__.__name__} -> {self.message}'
        else:
            return f'klasa {self.__class__.__name__} została użyta'
