# find the secret number in a range
found = False
secret_num = 10

for num in range(1, 11):
    if num == secret_num:
        print("secret number found!")
        found = True
if not found:
    print("Not found")