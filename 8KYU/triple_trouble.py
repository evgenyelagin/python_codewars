def triple_trouble(one, two, three):
    str = ""
    for a in one:
        str+=one

        for b in two:
            str += two

        for c in three:
                str += three
                
    print(str)


triple_trouble("aaa", "bbb", "ccc")