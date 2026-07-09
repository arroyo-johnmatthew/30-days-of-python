def main():
    user = input("Enter a text: ")
    count_vowels(user)

def count_vowels(text):
    counter = 0
    for char in text:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            counter += 1
    return counter

if __name__ == "__main__":
    main()