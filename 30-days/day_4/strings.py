string_one =  "Coding "
string_two = "For "
string_three = "All "
company = " Coding For All "
result = string_one + string_two + string_three

sentence = """You cannot end a sentence with because because 
            because is a conjunction"""

print(company)
print(len(company), "\n")

print(company.upper())
print(company.lower(), "\n")

print(company.capitalize())
print(company.title())
print(company.swapcase(), "\n")

company_sliced = company[6:14]
print(company_sliced)
print(company.find("Coding"))
print(company.replace("Coding", "Python"), "\n")

print(company.replace("All", "Everyone"))
print(company.split(", "))

print(company[10])
print(company.index('C'))
print(company.index('F'))
print(company.rfind('I'))

print(sentence.find("because"))
print(sentence.rindex("because"))

sliced_sentence = sentence[31:68]
print(sliced_sentence)
print(sliced_sentence.find("because"))

print(company.strip())

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

python_lan = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_lan))

print("I am enjoying this challenge \nI just wonder what is next \n")

print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFindland\tHelsinki")

radius = 10 
area = 3.14 * radius ** 2
print(f"The area of a circle with radius of {radius} is {area} meters square")

