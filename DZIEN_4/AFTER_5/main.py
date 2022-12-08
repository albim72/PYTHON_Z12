from time import sleep
from concurrent.futures import ThreadPoolExecutor as tpe, ProcessPoolExecutor as ppe
from after_five import return_msg_5

def main():
    pool = ppe(3)
    future = pool.submit(return_msg_5,"to jest komunikat 45")
    print(future.done())
    sleep(5)
    print(future.done())
    print(future.result())
    print(future.done())

def second():
    pool = tpe(3)
    future = pool.submit(return_msg_5,"to jest komunikat 45")
    print(future.done())
    sleep(5)
    print(future.done())
    print(future.result())
    print(future.done())

if __name__ == "__main__":
    second()
