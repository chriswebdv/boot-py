s = "abcaaaa"
letter = ""
count = 0
for char in s:
    if char not in letter:
        letter += char
        count += 1
print(count)