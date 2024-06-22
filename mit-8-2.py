def is_triangular(n):
    total = 0
    for i in range(n):
        total += i
        if total == n:
            print(True)
    print(False)

is_triangular(4)