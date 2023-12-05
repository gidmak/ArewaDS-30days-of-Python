# Day 7 of 30 Days of Python

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Find the length of the set it_companies
print(len(it_companies))    # 7

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)         # {'Amazon', 'Apple', 'Oracle', 'Twitter', 'IBM', 'Facebook', 'Microsoft', 'Google'}

# Insert multiple IT companies at once to the set it_companies
it_companies.update({"Flutterwave", "Paypal", "Paywizzard"})
print(it_companies)         # {'Oracle', 'Twitter', 'Microsoft', 'Paypal', 'Apple', 'Amazon', 'Google', 'Paywizzard', 'Facebook', 'IBM', 'Flutterwave'}   

# Remove one of the companies from the set it_companies
it_companies.pop()
print(it_companies)         # {'Oracle', 'Paywizzard', 'Google', 'IBM', 'Flutterwave', 'Apple', 'Microsoft', 'Facebook', 'Amazon', 'Twitter'}

# What is the difference between remove and discard
it_companies.remove({"Pinta"})  # Key Error
print(it_companies)

it_companies.discard({"Pinta"})
print(it_companies)             # No error raised

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Join A and B
print(A.union(B))           # {19, 20, 22, 24, 25, 26, 27, 28}

# Find A intersection B
print(A.intersection(B))    # {19, 20, 22, 24, 25, 26}

# Is A subset of B
print(A.issubset(B))        # True

# Are A and B disjoint sets
print(A.isdisjoint(B))      # False

# Join A with B and B with A
print(A.union(B))           # {19, 20, 22, 24, 25, 26, 27, 28}
print(B.union(A))           # print(B.union(A))

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))    # {27, 28}

# Delete the sets completely
del A,B
