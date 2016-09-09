

listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#listOne = [7, 3, 6, 10, 2, 8, 4, 1, 9, 5]


def is_sorted(listOne):
    return sorted(listOne) == listOne

print is_sorted(listOne)

