import random

def spin_slot():
    combo = ["🍒", "🍌", "🍎"]
    result = []

    for _ in range(3):
        result.append(random.choice(combo))
    return result
    
def slot_prizes(spin, bet):
    if spin[0] == spin[1] == spin[2]:
        if spin[0] == "🍒":
            return bet * 5
        elif spin[0] == "🍌":
            return bet * 10
        elif spin[0] == "🍎":
            return bet * 15
    return 0

def main():
    balance = 100

    # Slot machine starts
    while True:
        print("****************************")
        print("Welcome to Misty's Gamble")
        print("      🍒 🍌 🍎          ")
        print("****************************")
        
        print(f"\nCurrent Balance: {balance}")
        bet = int(input("Place your bet: "))
        print("")
        

        # Check if balance is less than or equal to zero
        if balance <= 0:
            print("No more balance... goodbye")
            print("")
            break

        # Check if bet is bigger than balance
        if bet > balance:
            print("Insufficient amount")
            print("")
            continue

        # Subtract the balance from the bet
        balance -= bet

        # If balance is ok, then proceed to roll the slot machine
        spin = spin_slot()
        
        # Check if the spin is winnable or not
        prize = slot_prizes(spin, bet)

        # Append the prize to the balance
        balance += prize

        # Print the overall result 
        print("".join(spin))
        print("You won", prize)
        
main()