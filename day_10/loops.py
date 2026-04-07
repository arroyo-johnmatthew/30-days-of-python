# --------------------------- EXERCISE LEVEL 1 ---------------------------------
# # Count 1 - 10
# count = 1
# while count < 11:
#     print(count)
#     count += 1

# # Count 10 - 1
# for item in range(10, 1, -1):
#     print(item)

# #
# ##
# ###
# ####
# #####         Expected output
# ######
# ####### 

# result = "#"
# while len(result) < 8:
#     print(result)
#     result += "#"

# # # # # # # # # 
# # # # # # # # # 
# # # # # # # # # 
# # # # # # # # #  
# # # # # # # # #  Expected Output
# # # # # # # # # 
# # # # # # # # # 
# # # # # # # # # 

# for col in range(8):
#     for row in range(8):
#         print("#", end=" ")
#     print("")

# # Iterate through the list
# python_list = ["Python", "Flask", "Django", "FASTAPI", "Panda"]
# for item in python_list:
#     print(item, end=" ")

# # 0 - 100 only print even numbers
# for num in range(0, 101):
#     if num % 2 == 0:
#         print(num)

# # 0 - 100 only print odd numbers
# for num in range(0, 101):
#     if num % 2 != 0:
#         print(num)

# --------------------------- EXERCISE LEVEL 2 ---------------------------------
# Print the sum of all numbers from 0 - 100
number = 0
for num in range(101):
    number += num

print("The total number:", number)

even = 0
odd = 0
for num in range(101):
    if num % 2 == 0:
        even += num
    elif num % 2 != 0:
        odd += num

print("The total even:", even)
print("The total odd:", odd)


