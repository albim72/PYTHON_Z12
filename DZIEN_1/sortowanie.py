zestaw_classic = ['samolot','aktor','miecz','mecz','Mieczysław','Gdańsk','anakonda','zenit',
                  'zakamarki','piorun','atak','macierz','wędka','wedle']

def bsort_classic(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i].lower() < a[i-1].lower():
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp

bsort_classic(zestaw_classic)
print(zestaw_classic)

zestaw_modern = ['samolot','aktor','miecz','mecz','Mieczysław','Gdańsk','anakonda','zenit',
                  'zakamarki','piorun','atak','macierz','wędka','widelec','wedle','Ń','ń']

def bsort_modern(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i].lower() < a[i-1].lower():
                a[i-1],a[i] = a[i],a[i-1]

bsort_modern(zestaw_modern)
print(zestaw_modern)
