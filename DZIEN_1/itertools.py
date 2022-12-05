import itertools

#przypadek 1
#operator nieskończony

for i in itertools.count(5,5):
    if i == 15:
        break
    else:
        print(f"i wynosi {i}")

#przypadek 2 -> cykle
count = 0
for i in itertools.cycle('AB'):
    if count > 3:
        break
    else:
        print(f"i = {i}")
        count += 1
        
