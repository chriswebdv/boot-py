# create random function that returns rock, paper or scissors as output
import random

# create list
rps = ["rock", "paper", "scissors"]

def computer_answer(answer):
    for i in rps:
        choice = random.choice(rps)
    return choice

print(computer_answer(rps))




# Create while loop that limits the user to 5 games and counts each game to determine a general winner 
# of the tournament
# inside the while loop create a conditional statement to detemine who wins each match and count the winners 
# per match

