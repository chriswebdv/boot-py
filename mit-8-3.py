def apply(criteria, n):
    for i in range(n):
        if i == criteria:
            i += 1
    print(i)


def criteria(n):
    if type(n) == "int":
        return True
    else:
        return False


apply(criteria, 20)