

def add_list_of_ints(l1, l2):
    r = []
    for a,b in zip (l1, l2):
        r.append(a+b)
    return r


def add(a, b):
    """Adds 2 corresponding lists of lists of ints. Assumes the inner list is integers, and that the lengths match"""
    assert len(a) == len(b)

    r = []
    for j, k in zip(a, b):
        if type(a) == list:
            r.append(add_list_of_ints(j,k))

    return r



m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
m3 = [[9, 10], [11, 12]]

assert add(m1, m2) == [[6, 8], [10, 12]]
