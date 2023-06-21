def fake_bin(x):
    s = ''
    for i in x:
        if i < '5':
            s += '0'
        if i == '5':
            s += '1'
        if i > '5':
            s += '1'
        print(s)
    return s

fake_bin("123456789")
