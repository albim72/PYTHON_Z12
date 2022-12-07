from functools import singledispatch
from decimal import Decimal

@singledispatch
def add(a,b):
    raise NotImplementedError('niewłaściwy typ danych')

@add.register(int)
def _(a,b):
    print(f"pierwszy argument funckji jest typu : {type(a)}")
    print(a+b)

@add.register(str)
def _(a,b):
    print(f"pierwszy argument funckji jest typu : {type(a)}")
    print(a+b)

@add.register(list)
def _(a,b):
    print(f"pierwszy argument funckji jest typu : {type(a)}")
    print(a+b)

@add.register(float)
@add.register(Decimal)
def _(a,b):
    print(f"pierwszy argument funckji jest typu : {type(a)}")
    print(a+b)

@add.register(float)
@add.register(int)
def _(a,b):
    print(f"pierwszy argument funckji jest typu : {type(a)}")
    print(a+b)


def main():
    add(2,7)
    add('Python','libraries')
    add([3,7,3],[9,7,3])
    add(2.44,15.7)
    add(Decimal(100.5),Decimal(14.56))
    add(7,6.7)

if __name__ == '__main__':
    main()
