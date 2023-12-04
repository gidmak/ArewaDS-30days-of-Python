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

# # Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Markus', "Hauwa")
print(family_members)

# Unpack siblings and parents from family_members
parents = family_members[-2:]
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("orange", "mango", "cashew", "banana")
vegetables = ("onions", "bitter leaf", "moringa")
animal_products = ("eggs", "meat")

food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(len(food_stuff_lt))
print(food_stuff_lt)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_lt[4:5]
print(middle_item)

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[6:])

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)        # False

# Check if 'Iceland' is a nordic country
print("Iceland" in nordic_countries)        # True
