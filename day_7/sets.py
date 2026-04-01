# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# --------------------------- EXERCISE 1 -----------------------------------

print("The length of the IT company is: ", len(it_companies))

# add twitter to the set
it_companies.add("Twitter")

# insert multiple IT companies 
it_companies.update(["Blazer", "ITech", "Geek Squad"])

# remove one of the companies from the set
it_companies.pop()

# --------------------------- EXERCISE 2 -----------------------------------

# combine set A and B
merged_set  = A.union(B)

# find intersection of A and B
A.intersection(B)

# a subset of B?
A.issubset(B)

# disjoint set?
A.isdisjoint(B)

# join A and B and vice versa
A.union(B)
B.union(A)

# symmetric difference
A.symmetric_difference(B)

# delete the sets
del A, B

# --------------------------- EXERCISE 3 -----------------------------------

# turn list into set and compare list & set size
set_of_ages = set(age)
print(len(age) > len(set_of_ages))

# find the unique word of
sentence = "I am a teacher and I love to inspire and teach people."
split_sentence = set(sentence.split())
