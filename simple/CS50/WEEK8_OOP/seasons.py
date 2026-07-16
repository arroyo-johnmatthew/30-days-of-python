import re
import sys
from datetime import date

def main():
    stdr_dt = r"^([1-9][0-9]{3})-((?:0[1-9]|1[0-2]))-((?:0[1-9]|[12][0-9]|3[01]))$"
    birthdate = input("Date of Birth: ")
    
    if (bday := validate_bday(birthdate, stdr_dt)):
        print("True")
    else:
        sys.exit("Invalid date")

def validate_bday(bday, standard):   
    matches = re.search(standard, bday)
    return matches

if __name__ == "__main__":
    main()