def is_triangular(n):
    total = 0
    for i in range(n):
        total += i
        if total == n:
            print(True)
        else:
            print(False)

print(is_triangular(4))
print(is_triangular(6))
print(is_triangular(1))