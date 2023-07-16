import prime_operations
from decimal import Decimal

__DEC_0 = Decimal(0)
__DEC_1 = Decimal(1)
__DEC_2 = Decimal(2)

def __decimal_floor(number):
    return (number - number % 1).normalize()

def __check_theta(theta):
    n = __DEC_1
    while True:
        last_generated_number = __decimal_floor(theta[0] ** (n / theta[1]))
        if not prime_operations.is_prime(int(last_generated_number)):
            return (last_generated_number, n)
        n += __DEC_1

def __validate_power_accuracy(theta, power):
    calculated_theta = theta[0] ** (__DEC_1 / theta[1])
    if power % theta[1] == __DEC_0:
        power += 1
    critical_number = __decimal_floor(calculated_theta ** power)
    if power % theta[1] != __DEC_0 and __decimal_floor(calculated_theta.next_minus() ** power) < critical_number:
        raise Exception(f'Error! Decimal precision is not enough anymore!: '
                        f'{calculated_theta} ** {power} ~= {__decimal_floor}')
    if __decimal_floor(calculated_theta.next_plus() ** power) > critical_number:
        raise Exception(f'Error! Decimal precision is not enough anymore!: '
                        f'{calculated_theta} ** {power} ~= {critical_number}')

biggest_power = 0
theta = (__DEC_2, __DEC_1)
check_index = 0
while True:
    (last_generated_number, failed_n) = __check_theta(theta)

    if failed_n - 1 > biggest_power:
        biggest_power = failed_n - 1

    print(f"Check index: {check_index:,}")
    print(f"Theta value: {theta[0] ** (__DEC_1 / theta[1]):,}")
    print(f"Theta form: {theta[0]:,} ^ 1/{theta[1]}")
    print(f"Biggest worked power: {biggest_power}")
    print(f"Last number (failed): {last_generated_number:,}")
    print(f"Failed power: {failed_n}")
    print(f"Max prime: {prime_operations.max_prime:,}")
    print(f"Max distance: {prime_operations.max_distance:,}")
    print(f"Primes count: {len(prime_operations.primes_list):,}")
    print("----------------------------------------------------")

    __validate_power_accuracy(theta, biggest_power)

    next_prime_number = Decimal(prime_operations.next_prime(int(last_generated_number)))
    theta = (next_prime_number, failed_n)
    check_index += 1
