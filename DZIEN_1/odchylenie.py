liczby = [56,59,90,88,97,67,69,77,75,74,59,61,91,98,90,85,83,82,73,23,123]

#korzystając z listy liczby wyznacz wartości największą i najmniejszą jako procent średniej arytmetycznej

def get_sr_odchylenie(dane):
    avg = sum(dane)/len(dane)
    skalowanie = [x/avg for x in dane]
    skalowanie.sort(reverse=True)
    return skalowanie

longest, *middle, shortest = get_sr_odchylenie(liczby)

print(f'największa wartość: {longest: 0.0%}')
print(f'najmniejsza wartość: {shortest: 0.0%}')
