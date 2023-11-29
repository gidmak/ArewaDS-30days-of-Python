# Day 2 of 30 days of python

# Variable declaration
first_name = "Gideon"
last_name = "Markus"
full_name = "Gideon Markus"
country = "Nigeria"
city = "Kaduna"
age = 34
year = 1989
is_married = True
is_true = False
is_light_on = True
school, best_subject, phone_number = "GSS Rido", "Mathematics", 2348038657553

# Check variable types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(school))
print(type(best_subject))
print(type(phone_number))

# Checking the len of a variable
print(len(first_name))

# Compare length of first_name and length of last_name
print(f"The length of {first_name} is {len(first_name)} and length of {last_name} is {len(last_name)}")

# Simple calculation
num_one = 5
num_two = 4

total = num_one + num_two               # Addition
diff = num_one - num_two                # Subtraction
product = num_one * num_two             # Multiplication
division = num_one / num_two            # Division
remainder = num_two % num_one           # Modulus
exp = num_one ** num_two                # Exponential
floor_division = num_one // num_two     # Floor division

# Calculating area of circle
radius = 30 # Radius in meters
area_of_circle = 3.14 * (radius  ** 2)    # Area of a circle given by pi * radius exp 2
print(f"Area of circle is {area_of_circle}")

circum_of_circle = 2 * 3.14 * radius    # Circumference of a circle given by 2 * pi * radius
print(f"Circumference of circle is {circum_of_circle}")

# Calculate area of circle from user inputted radius
radius_2 = input("Enter the radius: ")
area_of_circle_2 = 3.14 * (radius_2 ** 2)
print(f"Area of new circle is {area_of_circle_2}")

# Getting inputs from user
fname = input("Enter your first name:")
lname = input("Enter your last name:")
country_name = input("Enter your country name:")
your_age = input("Enter your age: ")

# Show reserved keywords
print(help("keywords"))
