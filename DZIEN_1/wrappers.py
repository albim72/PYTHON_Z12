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

@pomiarczasu
def big_lista():
    sum([i**9 for i in range(10000000)])

big_lista()

lt = [i**9 for i in range(10000000)]
@pomiarczasu
def bl_2():
    sum(lt)

bl_2()
