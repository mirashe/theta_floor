import prime_operations
from decimal import Decimal

def __check_num(num):
    print(f"{num:,} is {prime_operations.is_prime(Decimal(num)):,}")

def test_is_prime():
    prime_operations.initialize()
    __check_num(2)
    __check_num(3)
    __check_num(4)
    __check_num(30)
    __check_num(73)
    __check_num(24)
    __check_num(19)
    __check_num(6)
    __check_num(25)
    __check_num(73*73)
    __check_num(1)
