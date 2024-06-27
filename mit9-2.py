L = [1,2,3,4,5]
def sum_and_prod():
    (sum,prod) = (0,1)
    for i in L:
        sum += i
        prod *= i
    return ((sum,prod))


print(sum_and_prod())