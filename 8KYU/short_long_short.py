def solution(a, b):
    s = ''
    if len(a) < len(b):
        s = a + b + a
        return s
    else:
        s = b + a + b
        return s


def solution_2(a, b):
    if len(a) < len(b):
        return (a + b + a)
    else:
        return (b + a + b)