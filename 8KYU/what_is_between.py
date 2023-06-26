def between(a, b):
    if a < b:
        numbers = list(range(a, b + 1))
        print(numbers)
    return numbers


def between_2(a, b):
    return [result for result in range(a, b + 1)]


def between_3(a, b):
    arr = []
    for i in range(a, b + 1):
        arr.append(i)
    return arr


between(1, 4)
