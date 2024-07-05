def remove_all(L, e):
    Lcopy = L[:]
    L.clear()

    for i in Lcopy:
        if i != e:
            L.append(i)
    print(L)


L = [1,2,2,2]
remove_all(L, 1)
