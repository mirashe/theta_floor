from ast import Tuple
import math
from decimal import Decimal, getcontext

Dec_0 = Decimal(0)
Dec_1 = Decimal(1)
Dec_2 = Decimal(2)
Dec_3 = Decimal(3)
Dec_4 = Decimal(4)
Dec_10 = Decimal(10)

max_prime = Dec_2
primes_set = {max_prime}
primes_list = [max_prime]

def decimal_floor(number):
    return number - number % 1

def is_prime(number):
    global max_prime

    if number < Dec_2:
        return False
    
    if number <= max_prime:
        return number in primes_set

    sqrt_num = number.sqrt()
    sqrt_num = sqrt_num.to_integral_value()

    for i in primes_list:
        if i > sqrt_num:
            break
        if number % i == Dec_0:
            return False

    if sqrt_num < max_prime:
        return True

    i = max_prime + Dec_2
    if i == Dec_4:
        i = Dec_3

    while True:
        if i > sqrt_num:
            return True
        if is_prime(i):
            max_prime = i
            primes_set.add(i)
            primes_list.append(i)

            if number % i == Dec_0:
                return False
        i += 2


def next_prime(number):
    if number < Dec_2:
        return Dec_2

    next_num = number + Dec_1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += Dec_1

def check_tetha(tetha):
    n = Dec_1
    while True:
        if n % Dec_10 == Dec_0:
            print(f"check_tetha: checking {n}")

        if not is_prime(decimal_floor(tetha[0] ** (n / tetha[1]))):
            print(f"check_tetha: check failed at {n}")
            return n
        n += Dec_1

tetha = (Dec_2, Dec_1)

while True:
    failed_n = check_tetha(tetha)
    last_generated_number = decimal_floor(tetha[0] ** (failed_n / tetha[1]))
    print(f"last_generated_number: {last_generated_number:,}")
    print(f"max prime: {max_prime:,}")
    next_prime_number = next_prime(last_generated_number)
    print(f"next_prime_number: {next_prime_number:,}")
    tetha = (next_prime_number, failed_n)
    print(f"tetha: {tetha} -> {tetha[0] ** (Dec_1 / tetha[1]):,}")

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
    check_num(73*73)
    check_num(1)
