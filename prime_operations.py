import math

import file_operations

primes_list = file_operations.read_integers_from_file()

if len(primes_list) == 0:
    primes_list = [2, 3]
    file_operations.write_to_file(2)
    file_operations.write_to_file(3)

print('Calculating the maximum distance between consecutive primes until now...')
max_distance = max([x - y for x, y in zip(primes_list[1:], primes_list[:-1])])
print('Finished!')

max_prime = primes_list[-1]

print('Making the prime numbers set using the list...')
__primes_set = set(primes_list)
print('Finished!')

def is_prime(number):
    global max_prime, max_distance

    if number < 2:
        return False

    if number <= max_prime:
        return number in __primes_set

    sqrt_num = math.floor(number ** 0.5)

    for i in primes_list:
        if i > sqrt_num:
            break
        if number % i == 0:
            return False

    if sqrt_num < max_prime:
        return True

    i = max_prime + 2

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

            if number % i == 0:
                return False
        i += 2


def next_prime(number):
    if number < 2:
        return 2

    if number % 2 == 0:
        next_num = number + 1
    else:
        next_num = number + 2

    while True:
        if is_prime(next_num):
            return next_num
        next_num += 2
