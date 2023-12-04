# Day 6 of 30 days of python

# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Sam', 'Paul', 'Henry', 'Emma', 'Joshua')
sisters = ('Grace', 'Esther')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ("Markus", "Hauwa")
family_members = siblings + parents
print(family_members)