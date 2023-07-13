import prime_operations
from decimal import Decimal

__DEC_0 = Decimal(0)
__DEC_1 = Decimal(1)
__DEC_2 = Decimal(2)
__DEC_10 = Decimal(10)

def __decimal_floor(number):
    return number - number % 1

def __check_tetha(tetha):
    n = __DEC_1
    while True:
        if n % __DEC_10 == __DEC_0:
            print(f"__check_tetha: checking {n}")

        if not prime_operations.is_prime(__decimal_floor(tetha[0] ** (n / tetha[1]))):
            print(f"__check_tetha: check failed at {n}")
            return n
        n += __DEC_1

def find_tetha():
    tetha = (__DEC_2, __DEC_1)
    check_index = 0
    while True:
        failed_n = __check_tetha(tetha)
        last_generated_number = __decimal_floor(tetha[0] ** (failed_n / tetha[1]))

        print(f"check index: {check_index:,}")
        print(f"last_generated_number: {last_generated_number:,}")
        print(f"max prime: {prime_operations.max_prime:,}")
        print(f"max distance: {prime_operations.max_distance:,}")
        print(f"primes count: {len(prime_operations.primes_list):,}")
        print("----------------------------------------------------")

        next_prime_number = prime_operations.next_prime(last_generated_number)
        print(f"next_prime_number: {next_prime_number:,}")
        tetha = (next_prime_number, failed_n)
        print(f"tetha: {tetha} -> {tetha[0] ** (__DEC_1 / tetha[1]):,}")
        check_index += 1
