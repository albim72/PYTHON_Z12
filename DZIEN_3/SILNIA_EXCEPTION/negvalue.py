class NagativeValue(Exception):
    def __init__(self,n):
        self.n = n

    def __str__(self):
        return f"zadana wartość n = {self.n}, wartość n nie może być ujemna!"
