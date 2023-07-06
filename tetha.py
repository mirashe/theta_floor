from ast import Tuple
import math
from decimal import Decimal, getcontext

def is_prime(number):
    if number < 2:
        return False

    sqrt_num = Decimal(number).sqrt()
    sqrt_num = sqrt_num.to_integral_value(context=getcontext().prec)

    for i in range(2, sqrt_num + 1):
        if number % i == 0:
            return False

    return True

def next_prime(number):
    if number < 2:
        return 2

    next_num = number + 1
    while True:
        if is_prime(next_num):
            return next_num
        next_num += 1

def check_tetha(tetha) -> int:
    n = 1
    while True:
        if n % 10 == 0:
            print(f"check_tetha: checking {n}")
        if not is_prime(math.floor(Decimal(tetha) ** n)):
            print(f"check_tetha: check failed at {n}")
            return n
        n += 1

tetha = 2

while True:
    failed_n = check_tetha(tetha)
    last_generated_number = math.floor(Decimal(tetha) ** failed_n)
    next_prime = next_prime(last_generated_number)
    tetha = 