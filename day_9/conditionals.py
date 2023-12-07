# Day 9 of 30 Days of Python

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
age = int(input("Enter your age: "))
if age >= 18: 
    print("You are old enough to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age
my_age = 34
your_age = int(input("Enter your age: "))
if my_age > your_age:
    if my_age - your_age > 1:
        print(f"I am {my_age - your_age} years older than you.")
    else:
        print(f"I am {my_age - your_age} year older than you.")
elif your_age > my_age:
    if your_age - my_age > 1:
        print(f"You are {your_age - my_age} years older than me.")
    else:
        print(f"You are {your_age - my_age} year older than me.")
else:
    print("We are age mates!")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = input("Enter number one: ")
b = input("Enter number two: ")
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")