# Kata: 5b16490986b6d336c900007d

def my_languages(results):
    res = [x for x in results.items() if x[1] >= 60]

    res.sort(reverse=True, key=lambda x: x[1])

    res = [x[0] for x in res]

    return res


def my_languages_2(results):
    return sorted((lang for lang, result in results.items() if result >= 60), reverse=True, key=results.get)


def my_languages_3(results):
    return [key for key, value in sorted(results.items(), key=lambda item: item[1], reverse=True) if value >= 60]


def run_tests():
    tests = [
        {"Java": 10, "Ruby": 80, "Python": 65},
        {"Hindi": 60, "Dutch": 93, "Greek": 71},
        {"C++": 50, "ASM": 10, "Haskell": 20},
    ]

    for test in tests:
        print(my_languages_3(test))


def driver():
    run_tests()


driver()
