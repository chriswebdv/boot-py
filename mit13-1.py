def pairwise_div(Lnum, Ldenom):
    assert L1 != [] or L2 != [], "You have an empty list"
    num_list = []
    for num, denom in zip(Lnum, Ldenom):
        try:
            total = num / denom
            num_list.append(total)
        except:
            raise ZeroDivisionError("You are dividing by zero")
        
    return num_list


L1 = [4,5,6]
L2 = [1,2,10]

print(pairwise_div(L1, L2))

