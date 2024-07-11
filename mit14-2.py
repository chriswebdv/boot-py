def find_in_list(ld, k):
    for dict in ld:
        if k in dict:
            return True
    return False
            
    

d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
print(find_in_list([d1,d2,d3], 7))
print(find_in_list([d1,d2,d3], 1))
