import re

email = input("Email: ").strip()

# '.' means any char
# '*' 0 or more chars
# '+' 1 or more chars
# '\' esc char, use to differentiate '.' and literal '.'
# '^' must match the start of the str
# '$' must match the end of the str
# '?' 0 or 1 chars, basically optional
# '[]' set of chars
# '[^]' complementing the set, for ex, '[^@]' means any string but not the '@'

# Additional symbols
# '\d' decimal digit
# '\D' not a decimal
# '\s' whitespace chars
# '\S' not a whitespace char
# '\w' word chars as well as nums and the underscore
# '\W' not a word char

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")