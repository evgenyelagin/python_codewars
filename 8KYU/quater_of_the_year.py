def quarter_of(month):
    if month <= 3:
        return 1
    if month <= 6 and month > 3:
        return 2
    if month <= 9 and month > 6:
        return 3
    else:
        return 4
