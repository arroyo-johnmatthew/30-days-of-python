import random

# one live bullet in a gun
chamber = [0, 0, 0, 0, 0, 1]

while True:
    choice = input("🔫 Fire a bullet? yes/no: ").lower()
    print("")

    if choice in ["no", "n"]:
        print("Goodbye!\n")
        break

    elif choice in ["yes", "y"]:
        # spins the chamber before getting a bullet
        shot = random.choice(chamber)

        if shot == 1:
            print("💀 You are Dead 💀\n")
            break
        else:
            print("You survived the shot 😰")
            print(f"bullets remaining: {len(chamber)}\n")
            continue