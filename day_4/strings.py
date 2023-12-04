# Day 4 of 30 Days of python

# Convert '30', 'days', 'of', 'python' to a single string
broken_strings1 = ['30', 'Days', 'Of', 'Python']
conc_string1 = ' '.join(broken_strings1)
print(conc_string1)

# Concatenate 'Coding' 'For' 'All' into a single string
broken_strings2 = ['Coding', 'For', 'All']
conc_string2 = ' '.join(broken_strings2)
print(conc_string2)

# Declare a variable named company and assign it to an initial value "Coding For All"
company = 'Coding For All'

# Print the variable company using print()
print(company)

# Print the length of the company string using len() method and print()
print(len(company))

# Change all the characters to uppercase letters using upper() method
print(company.upper())

# Change all the characters to lowercase letters using lower() method
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.title())
print(company.capitalize())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string
print(company[0])

# Check if Coding For All string contains a word Coding using the method index, find or other methods
print('Coding' in 'Coding For All')

# Replace the word coding in the string 'Coding For All' to Python
string = 'Coding For All'
print(string.replace('Coding', 'Python'))

# Change Python for Everyone to Python for All using the replace method or other methods.
statement = 'Python for Everyone'
print(statement.replace('Everyone', 'All'))

# Split the string 'Coding For All' using space as the separator (split()) .
statement = 'Coding For All'
print(statement.split(' '))

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
s_media = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(s_media.split(', '))

# What is the character at index 0 in the string Coding For All.
string = 'Coding For All'
print(string[0])

# What is the last index of the string Coding For All.
string = 'Coding For All'
print(string[-1])

# What character is at index 10 in "Coding For All" string.
string = 'Coding For All'
print(string[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = []
py_string = 'Python For Everyone'
split_string = py_string.split(' ')
for i in split_string:
    acronym.append(i[0])
print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.
py_string = 'Coding For All'
split_string = py_string.split()
acronym = ' '.join(i[0] for i in split_string)
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All.
challenge = 'Coding For All'
print(challenge.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All
challenge = "Coding For All"
print(challenge.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
challenge = 'Coding For All People'
print(challenge.rfind('l')-1)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
challenge = 'You cannot end a sentence with because because because is a conjunction'
print(challenge.index('because'))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
challenge = 'You cannot end a sentence with because because because is a conjunction'
sub_string = 'because'
print(challenge.rindex(sub_string))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
challenge = 'You cannot end a sentence with because because because is a conjunction'
print(challenge[30:55])

# Does ''Coding For All' start with a substring Coding?
challenge = 'Coding For All'
sub_string = 'Coding'
print(challenge.startswith(sub_string))

# Does 'Coding For All' end with a substring coding?
challenge = 'Coding For All'
sub_string = 'coding'
print(challenge.startswith(sub_string))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
challenge = '   Coding For All      '
print(challenge.strip())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_python_lib = ' '.join(python_libraries)
print(joined_python_lib)

# Use the new line escape sequence to separate the following sentences. I am enjoying this challenge.I just wonder what is next.
challenge = 'I am enjoying this challenge. \nI just wonder what is next.'
print(challenge)

# Use a tab escape sequence to write the following lines. Name      Age     Country   City Asabeneh  250     Finland   Helsinki
challenge = 'Name \t\tAge \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki'
print(challenge)

# Use the string formatting method to display the result:
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area}")

# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))