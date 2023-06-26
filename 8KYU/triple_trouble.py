def triple_trouble(one, two, three):
    str = "".join(a+b+c for a, b, c in zip(one, two, three))
    print(str)
    return str

triple_trouble("aaa", "bbb", "ccc")