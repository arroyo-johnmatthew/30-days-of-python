# --------------------------- EXERCISE LEVEL 1 -----------------------------------

# age = int(input("Enter your age: "))

# # code if condition else code SHORTHAND Method
# # print("You are old enough to learn how to drive") if age >= 18 else print("You need", 18 - age, "more years before you can drive!")

# if age >= 18:
#     print("You are old enough to learn to drive")
# else:
#     print("You need", 18 - age, "more years before you can drive!")

# my_age = 21
# your_age = int(input("Enter your age: "))

# if your_age > my_age:
#     if your_age - my_age == 1:
#         print("You are 1 year older than me!")
#     else:
#         print("You are", your_age - my_age, "years older than me")
# elif your_age < my_age:
#     if my_age - your_age == 1:
#         print("You are 1 year younger than me!")
#     else:
#         print("You are", my_age - your_age, "years younger than me")
# else:
#     print("We are the same age!")

# --------------------------- EXERCISE LEVEL 2 ---------------------------------

# grade = int(input("Enter your grade: "))

# if grade >= 90:
#     print("Your grade is A")
# elif grade <= 89 and grade >= 80:
#     print("Your grade is B")
# elif grade <= 79 and grade >= 70:
#     print("Your grade is C")
# elif grade <= 69 and grade >= 60:
#     print("Your grade is D")
# elif grade <= 59 and grade >= 50:
#     print("Your grade is F")
# else:
#     print("You seem to have no grades 😓")

# autumn = ("september", "october", "november")
# winter = ("december", "january", "february")
# spring = ("march", "april", "may")
# summer = ("june", "july", "august")

# month = input("Enter your month: ").lower()

# for item in autumn:
#     if month == item:
#         print("Current Season: Autumn")
    
# for item in winter:
#     if month == item:
#         print("Current Season: Winter")

# for item in spring:
#     if month == item:
#         print("Current Season: Spring")

# for item in summer:
#     if month == summer:
#         print("Current Season: Summer")  
# else: 
#     print("Invalid") 

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input("Add your fruit boi: ").lower()

# if fruit in fruits:
#     print("That fruit already exists!")
# else:
#     fruits.append(fruit)
#     print("The modified fruit: ", fruits)