import time
import concurrent.futures
from funkcja_prime import znajdz_sume_liczb_pierwszych

def first():
    numbers = [(1,10000),(3,50000),(5000,100000),(4,900),(800,15000)]
    print("___tryb synchroniczny_____")

    start_time = time.time()
    for pair in numbers:
        prime_sum = znajdz_sume_liczb_pierwszych(*pair)
        print(prime_sum)

    end_time = time.time()
    print(f'Czas całkowity -> tryb synchroniczny: {end_time - start_time:.2f} s')


print("___tryb asynchroniczny_____")
def run_heavy_function(params):
    return znajdz_sume_liczb_pierwszych(*params)
def main():
    numbers = [(1, 10000), (3, 50000), (5000, 100000), (4, 900), (800, 15000)]
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        result = executor.map(run_heavy_function,numbers)
    print(list(result))

    end_time = time.time()
    print(f'Czas całkowity -> tryb asynchroniczny: {end_time - start_time:.2f} s')

if __name__ == '__main__':
    first()
    main()

