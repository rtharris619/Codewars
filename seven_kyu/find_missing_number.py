import random


def missing_no(nums):
    for num in range(0, 101):
        if num not in nums:
            return num


def missing_no_2(nums):
    calc = 100*101//2
    return calc - sum(nums)


def generate_unsorted_numbers(first, last):
    nums = list(range(first, last))
    random.shuffle(nums)
    return nums


def driver():
    nums = generate_unsorted_numbers(0, 101)
    nums.remove(42)
    result = missing_no_2(nums)
    print(result)


driver()
