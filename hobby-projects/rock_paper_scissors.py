import random

computer = ("rock", "paper", "scissors")
comp = random.choice(computer)

while True:
    user = input("Enter your choice (rock/paper/scissors): ").lower()

    if user not in computer:
        print("Not a valid option. Try again")
        continue

    if user == "rock" and comp == "scissors":
        print("You won! computer chose", comp)
    elif user == "paper" and comp == "rock":
        print("You won! computer chose", comp)
    elif user == "scissors" and comp == "paper":
        print("You won! computer chose", comp)
    elif user == comp:
        print("Tie!")
    else:
        print("You lose! computer chose", comp)
