import re
import sys
from datetime import date

def main():
    birthdate = input("Date of Birth: ")
    format = get_format()
    validate_bday(birthdate, format)

def get_format():
    return r"^([1-9][0-9]{3})-((?:0[1-9]|1[0-2]))-((?:0[1-9]|[12][0-9]|3[01]))$"

def validate_bday(bday, format):   
    matches = re.search(format, bday)
    if (matches):
        return True
    else:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()