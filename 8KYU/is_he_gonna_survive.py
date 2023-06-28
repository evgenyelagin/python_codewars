def hero(bullets, dragons):
    if bullets / 2 >= dragons:
        return True
    else:
        return False

# можно упросить функцию
def hero2(bullets, dragons):
    return bullets / 2 >= dragons
