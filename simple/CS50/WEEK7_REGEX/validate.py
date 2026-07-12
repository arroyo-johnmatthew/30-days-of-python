import re

email = input("Email: ").strip()

# '.' means any char
# '*' 0 or more chars
# '+' 1 or more chars
# '\' esc char, use to differentiate '.' and literal '.'
# '^' must match the start of the str
# '$' must match the end of the str
# '[]' set of chars
# '[^]' complementing the set, for ex, '[^@]' means any string but not the '@'

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")