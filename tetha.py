import os
from decimal import Decimal, getcontext

prime_numbers_file_path = 'prime_numbers.txt'

DEC_0 = Decimal(0)
DEC_1 = Decimal(1)
DEC_2 = Decimal(2)
DEC_3 = Decimal(3)
DEC_4 = Decimal(4)
DEC_10 = Decimal(10)
DEC_1000 = Decimal(1000)

def read_decimals_from_file():
    if not os.path.isfile(prime_numbers_file_path):
        return []

    decimal_list = []
    with open(prime_numbers_file_path, 'r') as f:
        for line in f:
            decimal_list.append(Decimal(line.strip()))

    return decimal_list

def write_to_file(value):
    with open(prime_numbers_file_path, 'a') as f:
        f.write(str(value) + '\n')

def decimal_floor(number):
    return number - number % 1

def is_prime(number):
    global max_prime, max_distance

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
            if i - max_prime > max_distance:
                max_distance = i - max_prime

            max_prime = i
            primes_set.add(i)
            primes_list.append(i)
            write_to_file(i)

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

primes_list = read_decimals_from_file()
if len(primes_list) == 0:
    primes_list = [DEC_2]
    write_to_file(DEC_2)

max_distance = DEC_1  # Maximum observed distance between two consecutive prime numbers
max_prime = primes_list[-1]
primes_set = set(primes_list)

tetha = (DEC_2, DEC_1)
check_index = 0

while True:
    failed_n = check_tetha(tetha)
    last_generated_number = decimal_floor(tetha[0] ** (failed_n / tetha[1]))

    print(f"check index: {check_index:,}")
    print(f"last_generated_number: {last_generated_number:,}")
    print(f"max prime: {max_prime:,}")
    print(f"max distance: {max_distance:,}")
    print(f"primes count: {len(primes_list):,}")
    print("----------------------------------------------------")

    next_prime_number = next_prime(last_generated_number)
    print(f"next_prime_number: {next_prime_number:,}")
    tetha = (next_prime_number, failed_n)
    print(f"tetha: {tetha} -> {tetha[0] ** (DEC_1 / tetha[1]):,}")
    check_index += 1

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
