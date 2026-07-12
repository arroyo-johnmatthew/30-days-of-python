import re

email = input("Email: ").strip()

# '.' means any char
# '*' means 0 or more chars
# '+' means 1 or more chars
# '\' means esc char, use to differentiate '.' and literal '.'

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")