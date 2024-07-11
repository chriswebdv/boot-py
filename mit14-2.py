def find_in_list(ld, k):
    for dict in ld:
        for key in dict:
            if k in dict.keys():
                return True
            else:
                return False
    

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
print(find_in_list([d1,d2,d3], 2))
print(find_in_list([d1,d2,d3], 1))
