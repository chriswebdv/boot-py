secret_num = 8
ask = int(input("Give guess: "))

if ask == secret_num:
    print("the same!")
elif ask > secret_num:
    print("Too high!")
else:
    print("Too low!")