# Kata: 54c27a33fb7da0db0100040e
import math


def is_square(n):
    sqrt = math.sqrt(abs(n))
    if sqrt.is_integer() and sqrt * sqrt == n:
        return True
    return False


def is_square_2(n):
    return n >= 0 and math.sqrt(n).is_integer()


def run_test_cases(lst):
    for i in range(len(lst)):
        print(lst[i], "-", is_square_2(lst[i]))


def driver():
    run_test_cases([-1, 0, 3, 4, 25, 26])


driver()
