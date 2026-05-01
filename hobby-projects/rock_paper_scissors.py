import random

computer = ("rock", "paper", "scissors")
comp = random.choice(computer)

try: 
    while True:
        print("⚠️  Press ctrl + z + ENTER to exit")
        user = input("Enter your choice: rock | paper | scissors ").lower()
        print("")

        if user not in computer:
            print("⚠️  Not a valid option. Try again")
            continue
        
        if user == "rock" and comp == "scissors":
            print("🥳🙌  You won! computer chose", comp)
            print(" ")
        elif user == "paper" and comp == "rock":
            print("🥳🙌  You won! computer chose", comp)
            print(" ")
        elif user == "scissors" and comp == "paper":
            print("🥳🙌  You won! computer chose", comp)
            print(" ")
        elif user == comp:
            print("😱  Tie!")
            print(" ")
        else:
            print("😭😵  You lose! computer chose", comp)
            print(" ")
except EOFError:
    print()
