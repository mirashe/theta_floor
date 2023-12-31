import os

__prime_numbers_file_path = 'prime_numbers.txt'

def read_integers_from_file():
    if not os.path.isfile(__prime_numbers_file_path):
        return []

    print('Reading the pre-stored primes file...')

    integer_list = []
    with open(__prime_numbers_file_path, 'r') as f:
        for line in f:
            new_number = int(line.strip())
            if len(integer_list) > 0 and new_number <= integer_list[-1]:  # validate the numbers
                raise Exception(f'Error! Unexpected values found in the given file!: '
                                f'{integer_list[-1]}, {new_number}')
            integer_list.append(new_number)

    print('Finished!')
    return integer_list

__write_buffer = []
def write_to_file(value):
    global __write_buffer
    __write_buffer.append(value)
    if len(__write_buffer) < 10000:
        return

    with open(__prime_numbers_file_path, 'a') as f:
        for num in __write_buffer:
            f.write(str(num) + '\n')
    __write_buffer = []
