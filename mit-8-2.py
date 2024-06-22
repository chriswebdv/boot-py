def is_triangular(n):
    total = 0
    for i in range(n+1):
        total += i
        if total == n:
            return(True)
    
    return(False)

print(is_triangular(4))
print(is_triangular(6))
print(is_triangular(1))