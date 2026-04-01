# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("The length of the IT company is: ", len(it_companies))

# add twitter to the set
it_companies.add("Twitter")

# insert multiple IT companies 
it_companies.update(["Blazer", "ITech", "Geek Squad"])

# remove one of the companies from the set
it_companies.pop()
