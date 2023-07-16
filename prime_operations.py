import file_operations
from decimal import Decimal

__DEC_0 = Decimal(0)
__DEC_1 = Decimal(1)
__DEC_2 = Decimal(2)
__DEC_3 = Decimal(3)

primes_list = file_operations.read_decimals_from_file()

if len(primes_list) == 0:
    primes_list = [__DEC_2, __DEC_3]
    file_operations.write_to_file(__DEC_2)
    file_operations.write_to_file(__DEC_3)

print('Calculating the maximum distance between consecutive primes until now...')
max_distance = max([x - y for x, y in zip(primes_list[1:], primes_list[:-1])])
print('Finished!')

max_prime = primes_list[-1]

print('Making the prime numbers set using the list...')
__primes_set = set(primes_list)
print('Finished!')

def is_prime(number):
    global max_prime, max_distance

    if number < __DEC_2:
        return False

    if number <= max_prime:
        return number in __primes_set

    sqrt_num = number.sqrt()
    sqrt_num = sqrt_num.to_integral_value()

    for i in primes_list:
        if i > sqrt_num:
            break
        if number % i == __DEC_0:
            return False

    if sqrt_num < max_prime:
        return True

    i = max_prime + __DEC_2

    while True:
        if i > sqrt_num:
            return True
        if is_prime(i):
            if i - max_prime > max_distance:
                max_distance = i - max_prime

            max_prime = i
            __primes_set.add(i)
            primes_list.append(i)
            file_operations.write_to_file(i)

            if number % i == __DEC_0:
                return False
        i += __DEC_2


def next_prime(number):
    if number < __DEC_2:
        return __DEC_2

    if number % __DEC_2 == __DEC_0:
        next_num = number + __DEC_1
    else:
        next_num = number + __DEC_2

    while True:
        if is_prime(next_num):
            return next_num
        next_num += __DEC_2
