# --------------------------- EXERCISE LEVEL 1 -----------------------------------
# age = int(input("Enter your age: "))

# # code if condition else code SHORTHAND Method
# # print("You are old enough to learn how to drive") if age >= 18 else print("You need", 18 - age, "more years before you can drive!")

# if age >= 18:
#     print("You are old enough to learn to drive")
# else:
#     print("You need", 18 - age, "more years before you can drive!")

my_age = 21
your_age = int(input("Enter your age: "))

if your_age > my_age:
    if your_age - my_age == 1:
        print("You are 1 year older than me!")
    else:
        print("You are", your_age - my_age, "years older than me")
elif your_age < my_age:
    if my_age - your_age == 1:
        print("You are 1 year younger than me!")
    else:
        print("You are", my_age - your_age, "years younger than me")
else:
    print("We are the same age!")