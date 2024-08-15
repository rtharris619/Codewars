def some_but_not_all(seq, pred):
    results = []
    for i in range(len(seq)):
        results.append(pred(seq[i]))

    return any(results) and not all(results)


def some_but_not_all_2(seq, pred):
    return any(map(pred, seq)) and not all(map(pred, seq))


def run_tests(lst):
    for i in range(len(lst)):
        seq = lst[i][0]
        pred = lst[i][1]
        print(seq, "-", some_but_not_all_2(seq, pred))


def driver():
    lst = [
        ('abcdefg&%$', str.isalpha),
        ('&%$=', str.isalpha),
        ('abcdefg', str.isalpha),
        ([4, 1], lambda x: x > 3),
        ([1, 1], lambda x: x > 3),
        ([4, 4], lambda x: x > 3)
    ]
    run_tests(lst)


driver()
