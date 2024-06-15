where = input("Go left or right: ")
counter = 0
while where == "right":
    where = input("Go left or right: ")
    counter = counter + 1
    print(counter)
    if counter == 2:
        print("Sad face :()")
print("you are out!")
