def max(a, b):
    return a if a > b else b


I = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def max_list(a):
    head, *tail = a
    return max(head, max_list(tail)) if tail else head


print(max(3, 7))
print(max_list(I))
