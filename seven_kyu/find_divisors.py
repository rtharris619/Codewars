# Kata: 544aed4c4a30184e960010f4

def divisors(integer):

    divs = []
    for i in range(2, integer):
        if integer % i == 0:
            divs.append(i)

    if len(divs) == 0:
        return f"{integer} is prime"

    return divs


def divisors_2(integer):
    divs = [a for a in range(2, integer) if integer % a == 0]
    if len(divs) == 0:
        return f"{integer} is prime"
    return divs


def run_test_cases(lst):
    for i in lst:
        print(i, "-", divisors_2(i))


def driver():
    run_test_cases([12, 25, 13, 29])


driver()
