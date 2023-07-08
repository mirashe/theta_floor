from ast import Tuple
import math
from decimal import Decimal, getcontext

DEC_0 = Decimal(0)
DEC_1 = Decimal(1)
DEC_2 = Decimal(2)
DEC_3 = Decimal(3)
DEC_4 = Decimal(4)
DEC_10 = Decimal(10)
DEC_1000 = Decimal(1000)

max_prime = DEC_2
primes_set = {max_prime}
primes_list = [max_prime]

prime_check_window = DEC_1000
prime_check_top = DEC_3
prime_check_next_start = {DEC_2: 0}


def is_prime_cached(number):
    global prime_check_top

    if number < prime_check_top:
        if number in prime_check_next_start:
            return True
        return False

    check_range = {}
    check_current = prime_check_top
    while check_current < prime_check_top + prime_check_window:
        check_range[check_current] = 0
        check_current += DEC_1

    primes_to_check = list(prime_check_next_start.keys())

    while len(primes_to_check) > 0:
        current_prime = primes_to_check.pop(0)


def decimal_floor(number):
    return number - number % 1


def is_prime(number):
    global max_prime

    if number < DEC_2:
        return False

    if number <= max_prime:
        return number in primes_set

    sqrt_num = number.sqrt()
    sqrt_num = sqrt_num.to_integral_value()

    for i in primes_list:
        if i > sqrt_num:
            break
        if number % i == DEC_0:
            return False

    if sqrt_num < max_prime:
        return True

    i = max_prime + DEC_2
    if i == DEC_4:
        i = DEC_3

    while True:
        if i > sqrt_num:
            return True
        if is_prime(i):
            max_prime = i
            primes_set.add(i)
            primes_list.append(i)

            if number % i == DEC_0:
                return False
        i += 2


def next_prime(number):
    if number < DEC_2:
        return DEC_2

    next_num = number + DEC_1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += DEC_1


def check_tetha(tetha):
    n = DEC_1
    while True:
        if n % DEC_10 == DEC_0:
            print(f"check_tetha: checking {n}")

        if not is_prime(decimal_floor(tetha[0] ** (n / tetha[1]))):
            print(f"check_tetha: check failed at {n}")
            return n
        n += DEC_1


tetha = (DEC_2, DEC_1)

while True:
    failed_n = check_tetha(tetha)
    last_generated_number = decimal_floor(tetha[0] ** (failed_n / tetha[1]))
    print(f"last_generated_number: {last_generated_number:,}")
    print(f"max prime: {max_prime:,}")
    next_prime_number = next_prime(last_generated_number)
    print(f"next_prime_number: {next_prime_number:,}")
    tetha = (next_prime_number, failed_n)
    print(f"tetha: {tetha} -> {tetha[0] ** (DEC_1 / tetha[1]):,}")


def check_num(num):
    print(f"{num:,} is {is_prime(Decimal(num)):,}")


def test_is_prime():
    check_num(2)
    check_num(3)
    check_num(4)
    check_num(30)
    check_num(73)
    check_num(24)
    check_num(19)
    check_num(6)
    check_num(25)
    check_num(73 * 73)
    check_num(1)
