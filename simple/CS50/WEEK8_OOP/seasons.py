import re
import sys
from datetime import date

def main():
    # Get user birthdate, date regex through func calling
    birthdate = input("Date of Birth: ")
    format = get_format()

    # Validate user birthdate and get year,month,day individually
    validate_bday(birthdate, format)
    year, month, day = split_date(birthdate, format)
    birthdate = date(year, month, day)

    # Create date object then subtract it with the current date
    age_in_mins = get_age_in_min(date.today(), birthdate)
    
def get_age_in_min(current, bday):
    diff = current - bday
    return diff.days * 24 * 60

def get_format():
    return r"^([1-9][0-9]{3})-((?:0[1-9]|1[0-2]))-((?:0[1-9]|[12][0-9]|3[01]))$"

def split_date(bday, format):
    matches = re.search(format, bday)
    return int(matches.group(1)), int(matches.group(2)), int(matches.group(3))

def validate_bday(bday, format):   
    matches = re.search(format, bday)
    if not matches:
        sys.exit("Invalid date")

if __name__ == "__main__":
    main()