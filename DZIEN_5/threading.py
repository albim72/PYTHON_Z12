import threading

def printcube(liczba):
    print(f"Sześcian z liczby: {liczba} = {liczba**3}")

def printsquare(liczba):
    print(f"Kwadrat z liczby: {liczba} = {liczba**2}")


if __name__ == '__main__':
    t1 = threading.Thread(target=printsquare,args=(10,))
    t2 = threading.Thread(target=printcube,args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Wykonane!")
