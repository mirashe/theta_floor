from ast import Tuple
import math
from decimal import Decimal, getcontext

primes = set([2])
primes_list = [2]
max_prime = Decimal(2)

def is_prime(number):
    global max_prime

    if number < Decimal(2):
        return False
    
    if number <= max_prime:
        return number in primes

    sqrt_num = number.sqrt()

    for i in primes_list:
        if i > sqrt_num:
            break
        if number % i == Decimal(0):
            return False

    if sqrt_num < max_prime:
        return True

    i = Decimal(max_prime + 2)
    if i == 4:
        i = Decimal(3)

    while True:
        if i > sqrt_num:
            return True
        if is_prime(i):
            max_prime = i
            primes.add(i)
            primes_list.append(i)

            if number % i == Decimal(0):
                return False
        i += 2


def next_prime(number):
    if number < Decimal(2):
        return Decimal(2)

    next_num = number + Decimal(1)
    while True:
        if is_prime(next_num):
            return next_num
        next_num += Decimal(1)

def check_tetha(tetha):
    n = Decimal(1)
    while True:
        if n % Decimal(10) == Decimal(0):
            print(f"check_tetha: checking {n}")
        if not is_prime(Decimal(math.floor(tetha[0] ** (Decimal(n) / tetha[1])))):
            print(f"check_tetha: check failed at {n}")
            return n
        n += Decimal(1)

tetha = (Decimal(2), Decimal(1))

while True:
    failed_n = check_tetha(tetha)
    last_generated_number = Decimal(math.floor(tetha[0] ** (Decimal(failed_n) / tetha[1])))
    print(f"last_generated_number: {last_generated_number}")
    next_prime_number = next_prime(last_generated_number)
    print(f"next_prime_number: {next_prime_number}")
    tetha = (Decimal(next_prime_number), Decimal(failed_n))
    print(f"tetha: {tetha} -> {tetha[0] ** (Decimal(1) / tetha[1])}")

def check_num(num):
    print(f"{num} is {is_prime(Decimal(num))}")

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
