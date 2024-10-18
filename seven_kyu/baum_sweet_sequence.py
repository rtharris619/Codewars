# Kata: 5d2659626c7aec0022cb8006
# https://en.wikipedia.org/wiki/Baum%E2%80%93Sweet_sequence

def baum_sweet():
    n = -1
    while True:
        n += 1
        binary = bin(n)
        result = no_block_odd_length_consecutive_zeros(binary)

        yield result


def no_block_odd_length_consecutive_zeros(bin_str):

    for char in bin_str:
        print(char)

    return 0


def run_tests():
    # print(next(baum_sweet()))
    # print(baum_sweet())

    take = lambda gen, n: [next(gen) for _ in range(n)]

    print(take(baum_sweet(), 20))


def driver():
    run_tests()


driver()
