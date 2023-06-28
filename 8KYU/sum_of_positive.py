def positive_sum(arr):
    arr2 = []
    arr3 = []
    if arr == arr2:
        return 0
    else:
        arr.sort()  # захотелось отсортировать список
        print(arr)
        for i in arr:
            if i > 0:  # беру значение из списка и сравниваю
                arr3.append(i)
                print(arr3)
        arr3 = sum(arr3)
        print(arr3)
        return arr3


# переписал чуток по-другому
def positive_sum_2(arr):
    arr2 = []
    if arr == arr2:
        return 0
    else:
        arr.sort()
        for i in arr:
            if i > 0:
                arr2.append(i)
        return sum(arr2)


def positive_sum_3(arr):  # крутое чужое решение
    return sum(x for x in arr if x > 0)


positive_sum([-1, 1, 2, 3, 0, -4, 9])
