import prime_operations
from decimal import Decimal

__DEC_0 = Decimal(0)
__DEC_1 = Decimal(1)
__DEC_2 = Decimal(2)

def __decimal_floor(number):
    return (number - number % 1).normalize()

def __check_tetha(tetha):
    n = __DEC_1
    while True:
        last_generated_number = __decimal_floor(tetha[0] ** (n / tetha[1]))
        if not prime_operations.is_prime(last_generated_number):
            return (last_generated_number, n)
        n += __DEC_1

def __validate_power_accuracy(tetha, power):
    calculated_tetha = tetha[0] ** (__DEC_1 / tetha[1])
    if power % tetha[1] == __DEC_0:
        power += 1
    critical_number = __decimal_floor(calculated_tetha ** power)
    if power % tetha[1] != __DEC_0 and __decimal_floor(calculated_tetha.next_minus() ** power) < critical_number:
        raise Exception(f'Error! Decimal precision is not enough anymore!: '
                        f'{calculated_tetha} ** {power} ~= {__decimal_floor}')
    if __decimal_floor(calculated_tetha.next_plus() ** power) > critical_number:
        raise Exception(f'Error! Decimal precision is not enough anymore!: '
                        f'{calculated_tetha} ** {power} ~= {critical_number}')

def find_tetha():
    biggest_power = 0
    tetha = (__DEC_2, __DEC_1)
    check_index = 0
    while True:
        (last_generated_number, failed_n) = __check_tetha(tetha)

        if failed_n > biggest_power:
            biggest_power = failed_n

        print(f"check index: {check_index:,}")
        print(f"tetha: {tetha[0]:,} ^ 1/{tetha[1]} -> {tetha[0] ** (__DEC_1 / tetha[1]):,}")
        print(f"check failed at: {failed_n}")
        print(f"biggest observed power: {biggest_power}")
        print(f"last_generated_number: {last_generated_number:,}")
        print(f"max prime: {prime_operations.max_prime:,}")
        print(f"max distance: {prime_operations.max_distance:,}")
        print(f"primes count: {len(prime_operations.primes_list):,}")
        print("----------------------------------------------------")

        __validate_power_accuracy(tetha, biggest_power)

        next_prime_number = prime_operations.next_prime(last_generated_number)
        tetha = (next_prime_number, failed_n)
        check_index += 1
