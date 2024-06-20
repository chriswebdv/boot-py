import random

#Write a function with not arguments to guess a number from 1 - 100

def numbers_game():
    for i in range(100):
        x = random.randint(1, 100)
        return x

ask_user = int(input("Guess my secret number: "))
print(type(ask_user))

print(numbers_game())