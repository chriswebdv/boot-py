# create random function that returns rock, paper or scissors as output
import random

# create list
rps = ["rock", "paper", "scissors"]

def computer_answer(answer):
    for i in rps:
        choice = random.choice(rps)
    return choice

# Create while loop that limits the user to 5 games and counts each game to determine a general winner 
# of the tournament
# inside the while loop create a conditional statement to detemine who wins each match and count the winners 
# per match

computer_score = 0
human_score = 0
count = 0

print("-------------------------------")
print("Choose between paper, rock or scissors, write in lowercase: ")
human_input = input("Answer: ")
print(human_input)

while count <= 5:
    pass