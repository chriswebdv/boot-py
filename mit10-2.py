def remove_elem(my_list, num):
    my_list2 = []
    for i in my_list:
        print("first",my_list2)
        if i != num:
            print("second", my_list2)
            my_list2.append(i)
            print("third", my_list2)
    return my_list2


my_list = ["word", 2, 2, 3, 4]
num = 2
remove_elem(my_list, num)