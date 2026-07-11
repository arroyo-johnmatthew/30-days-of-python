import csv

#Example 1, READ
students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

                     #anonymous function  #param    #return value
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")

#Example 2, WRITE
name = input("Enter your name: ")
home = input("Wheres your home: ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"]) 
    writer.writerow({"name": name, "home": home})

# import sys

# def main():
#     check_arg_len(sys.argv)
#     print(count_loc(sys.argv[1]))

# def check_arg_len(item):
#     if len(item) < 2:
#         return sys.exit("Too few command-line arguments")
#     elif len(item) > 2:
#         return sys.exit("Too many command-line aguments")

# def count_loc(item):
#     if not item.endswith(".py"):
#         sys.exit("Not a Python File")

#     count = 0

#     try:
#         with open(item, "r") as file:
#             for line in file:
#                 line = line.strip()

#                 # Checks for comments, whitespaces, docstrings
#                 if line == "":
#                     continue
#                 elif line.startswith("#"):
#                     continue
#                 else:
#                     count += 1

#     except FileNotFoundError:
#         sys.exit("File not Found")

#     return count

# if __name__ == "__main__":
#     main()
