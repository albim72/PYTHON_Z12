def trace(funkcja):
    def wrapper(*args,**kwargs):
        wynik = funkcja(*args,**kwargs)
        print(f'{funkcja.__name__}({args!r},{kwargs!r})'
              f'->{wynik!r}')
        return wynik
    return wrapper

@trace
def fibonacci(n):
    if n in (0,1):
        return n
    return (fibonacci(n-2)+fibonacci(n-1))


print(fibonacci(9))
