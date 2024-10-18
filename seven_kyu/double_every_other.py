
def double_every_other(lst):

    for i in range(1, len(lst), 2):
        lst[i] *= 2

    return lst


def double_every_other_2(lst):
    return [num * 2 if index % 2 != 0 else num for index, num in enumerate(lst)]


def driver():
    lst = [1, 2, 3, 4]
    result = double_every_other_2(lst)
    print(result)


driver()
