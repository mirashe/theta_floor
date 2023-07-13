import os
from decimal import Decimal

__prime_numbers_file_path = 'prime_numbers.txt'

def read_decimals_from_file():
    if not os.path.isfile(__prime_numbers_file_path):
        return []

    decimal_list = []
    with open(__prime_numbers_file_path, 'r') as f:
        for line in f:
            decimal_list.append(Decimal(line.strip()))

    return decimal_list

write_buffer = []
def write_to_file(value):
    global write_buffer
    write_buffer.append(value)
    if len(write_buffer) < 10000:
        return

    with open(__prime_numbers_file_path, 'a') as f:
        for num in write_buffer:
            f.write(str(num) + '\n')
    write_buffer = []

