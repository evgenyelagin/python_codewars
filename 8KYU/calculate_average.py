def find_average(numbers):
    if numbers == []:
        return 0
    else:
        return sum(numbers)/len(numbers)

def find_average_2(numbers):
    empty = []
    if empty == numbers:
        return 0
    else:
        s = sum(numbers)
        avg = s/len(numbers)
        return avg