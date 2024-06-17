s = "abca"
letter = ""
count = 0
for char in s:
    letter += char
    if letter != char:
      count += 1
print(count)
