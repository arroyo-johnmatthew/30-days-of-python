import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(address):    
    # Assign the pattern into a var with these ranges: 0-99|100-199|200-249|250-255
    ptrn = r"([1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"

    matches = re.search(fr"^{ptrn}\.{ptrn}\.{ptrn}\.{ptrn}$", address, re.IGNORECASE)
    if matches:
        return True
    else:
        return False

if __name__ == "__main__":
    main() 