# Day 5 of 30 Days of python

# # Declare an empty list
# empty_list = []

# Declare a list with more than 5 items
list_more_than_five = ["arsenal", "liverpool", "manchester city", "aston villa", "tottenham"]

# # Find the length of your list
# print(len(list_more_than_five))

# # Get the first item, the middle item and the last item of the list
# print(list_more_than_five[::2])

# # Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# mixed_data_types = ['Gideon', '34', '6.9', 'married', 'kaduna']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[::3])

# Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Flutterwave')

# Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Metaverse')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined_it_companies = '; '.join(it_companies)
print(joined_it_companies)

# Check if a certain company exists in the it_companies list.
print('WhatsApp' in it_companies)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
print(it_companies[4:5])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
del it_companies[3:5]
print(it_companies)

# Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end[:]
full_stack.insert(4, ['Python', 'SQL'])
print(full_stack)