def count_matches(d):
    count = 0
    for k,v in d.items():
        if k == v:
            count += 1
    return count



#Example
d = {1:2, 3:4, 5:6, 7:7}
print(count_matches(d))

d = {1:2, "a":"a", 5:5, "m":"m"}
print(count_matches(d))
