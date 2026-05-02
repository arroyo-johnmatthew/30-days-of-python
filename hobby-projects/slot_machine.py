import random

def spin_slot():
    combo = ["🍒", "🍌", "🍎"]
    result = []

    for _ in range(3):
        result.append(random.choice(combo))
    
    result = " ".join(result)
    return result

def print_slot():
    pass

def main():
    balance = 100

    # Slot machine starts
    while True:
        print("****************************")
        print("Welcome to Misty's Gamble")
        print("****************************")
        print("🍒 🍌 🍎")
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
        print(spin)
        
main()