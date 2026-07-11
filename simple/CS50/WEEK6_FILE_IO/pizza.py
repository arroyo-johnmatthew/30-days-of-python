import csv
import sys
from tabulate import tabulate

table = []

# Checks if the arg is too many or few
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Checks if the arg is a .csv file
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

# Checks if the file exists
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)

    print(tabulate(table, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File not Found")


# The file reading process is, it first reads regular.csv
# Then use DictReader to read the columns, assign it to reader var
# Iterate the reader var to append each items into the table list
# Take note: table.append can just use "row" as argument, 
# I just made the code longer so that you know whats happening behind the scenes