import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(address):
    matches = re.search(r"", address, re.IGNORECASE)

    if matches:
        return True
    else:
        return False

if __name__ == "__main__":
    main()