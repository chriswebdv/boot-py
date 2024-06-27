def remove_elem(my_list, num):
    my_list2 = []
    for i in range(len(my_list)):
        if num != my_list[i]:
            my_list2.append(num)

    return my_list2


my_list = ["word", 2, 2, 3, 4]
num = 2
print(remove_elem(my_list, num))