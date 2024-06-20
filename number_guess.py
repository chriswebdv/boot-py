import random

#Write a function with not arguments to guess a number from 1 - 100
ask_user = int(input("Guess my secret number: "))

def numbers_game():
    for i in range(100):
        x = random.randint(1, 100)
        return x

print(numbers_game())


while ask_user != numbers_game():
    if ask_user > numbers_game():
        print("Too high!")


