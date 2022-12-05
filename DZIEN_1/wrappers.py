#przykład 1
import math
import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f"czas wykonania funkcji: {endtime-starttime} s")
    return wrapper


def sleep(funkcja):
    def wrapper():
        time.sleep(3)
        funkcja()
    return wrapper

@pomiarczasu
@sleep
def big_lista():
    sum([i**9 for i in range(10000000)])

big_lista()

lt = [i**9 for i in range(10000000)]
@pomiarczasu
def bl_2():
    sum(lt)

bl_2()


#przypadek 2
def decorator_f(wrapped_function):
    def wrapper(a,b,*args,**kwargs):
        return wrapped_function(a,b,*args,**kwargs)
    return wrapper
@decorator_f
def wrapped_function(a,b,*args,**kwargs):
    print("wnętrze funkcji opakowanej")
    print(f'a={a}, b={b}')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')

a = 19
b = 44
wrapped_function(a,b,30,55,c=90,f=109)

#przypadek 3

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f'wołana funkcja: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(i):
    print(f"informacja: {i}")

info("bardzo ważne słowo...")

#przypadek 4
def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeater(n=6)
def komunikat(k,n):
    print(f"wynik dzielennia: {n/k}")

komunikat(45,67)
