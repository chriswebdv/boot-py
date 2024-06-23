import random

#Write a function with not arguments to guess a number from 1 - 100

def numbers_game():
    for i in range(100):
        x = random.randint(1, 50)
        return x


ask_user = int(input("Guess my secret number: "))

while ask_user != numbers_game():
    if ask_user > numbers_game():
        print(f"The correct number is {numbers_game()} Too high!")
        ask_user = int(input("Guess my secret number: "))
    elif ask_user < numbers_game():
        print(f"The correct number is {numbers_game()} Too low!")
        ask_user = int(input("Guess my secret number: "))

print("Correcto Mundo! You guessed right")
