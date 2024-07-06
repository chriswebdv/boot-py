def pairwise_div(Lnum, Ldenom):
    num_list = []
    for num, denom in zip(Lnum, Ldenom):
        try:
            total = num / denom
            num_list.append(total)
        except:
            raise ZeroDivisionError("You are dividing by zero")


L1 = [4,5,6]
L2 = [1,2,0]

