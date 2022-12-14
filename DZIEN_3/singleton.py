class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass(metaclass=Singleton):pass
class Potomna(SingletonClass):pass
class RegularClass:pass

a = RegularClass()
b = RegularClass()
print(a==b)

x = SingletonClass()
y = SingletonClass()

print(x==y)

px = Potomna()
py = Potomna()

print(px==py)
