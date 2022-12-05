#przypadek 1

def liczby():
    for i in range(17):
        yield i

print(liczby())
for p in liczby():
    print(p)

#przypadek 2

def wznowienie(n,k):
    print("wstrzymanie działania....")
    yield 1001
    print("wznowienie działania....")

    print("wstrzymanie działania....")
    yield n+k
    print("wznowienie działania....")

    print("wstrzymanie działania....")
    yield n-k
    print("wznowienie działania....")

    print("wstrzymanie działania....")
    yield n*k
    print("wznowienie działania....")

for i in wznowienie(6,8):
    if i == 1001:
        continue
    print(f'zwrócono wartość: {i}')
