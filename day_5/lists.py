# Exercise 1

# container = ["One Piece", "Bleach", "Naruto", "Dragon Ball", "Gintama"]
# mixed_data_types = ["Matthew", 21, "5'5", "Single", {"address": "Pasay City"}]
# it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# front_end = ["HTML", "CSS", "JavaScript", "React", "Redux"]
# back_end = ["Node", "Express", "MongoDB"]

# print(len(container))
# print(container[0], container[2], container[4])

# print(it_companies, "List Length: ", len(it_companies))

# it_companies.append("Accenture")
# print(it_companies)

# it_companies.insert(4, "InfoSys")
# print(it_companies)

# print(it_companies[6].upper())
# print('# '.join(it_companies))

# print("Roblox" in it_companies)

# print(sorted(it_companies))
# print(sorted(it_companies, reverse=True))

# print(it_companies[0:3])
# print(it_companies[-3:])
# print(it_companies[4:])

# print("📝 Current list: ", it_companies)

# print(it_companies.pop(0))
# print(it_companies.pop(4))

# it_companies.clear()
# print(it_companies)

# del it_companies

# full_stack = front_end + back_end
# print(full_stack)

# full_stack.insert(5, "Python")
# full_stack.insert(6, "SQL")
# print(full_stack)


# Exercise 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sorted_ages = sorted(ages)
min_age = min(ages)
max_age = max(ages)
median = (sorted_ages[4] + sorted_ages[5]) / 2
average = sum(sorted_ages) / len(sorted_ages)

print(sorted_ages)
print(median)
print(average)
print(max_age - min_age)

print(abs(min_age), abs(max_age))

