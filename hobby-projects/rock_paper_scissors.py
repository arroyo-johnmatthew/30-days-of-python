import random

user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
computer = ("rock", "paper", "scissors")
comp_choice = random.choice(computer)

if user_choice == "rock" and comp_choice == "scissors":
    print("You won! computer chose", comp_choice)
elif user_choice == "paper" and comp_choice == "rock":
    print("You won! computer chose", comp_choice)
elif user_choice == "scissors" and comp_choice == "paper":
    print("You won! computer chose", comp_choice)
elif user_choice == comp_choice:
    print("Tie!")
else:
    print("You lose! computer chose", comp_choice)
