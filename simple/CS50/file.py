#import csv

# Example 1, READ
# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})

#                      #anonymous function  #param    #return value
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

# Example 2, WRITE
# name = input("Enter your name: ")
# home = input("Wheres your home: ")

# with open("students.csv", "a") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"]) 
#     writer.writerow({"name": name, "home": home})

import sys
from pygount import SourceAnalysis

# Checks if the argument is few or too many
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line aguments")

# Checks if the FILENAME exists in the directory
try:
    analysis = SourceAnalysis.from_file(sys.argv[1], "pythonfile") # type: ignore
except FileNotFoundError:
    sys.exit("File does not exist")

# Checks if the argument (FILENAME) is a python file
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")

# If all is well, write the output to the python file
with open(sys.argv[1], "a") as file:
    file.write(f"# {analysis.code_count}") # type: ignore