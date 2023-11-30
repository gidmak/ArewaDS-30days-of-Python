# Day 3 of 30 days of python

# Declare age as an integer
my_age = 34

# Declare my height as a float
my_height = 89.32

# Declare a variable that stores a complex number
c_num = 3 + 1j

# Calculating the area of a triangle
print("You are about to calculate the area of a triangle")
t_base = float(input("Enter the base: "))
t_height = float(input("Enter the height: "))
area_of_triangle = 0.5 * t_base * t_height
print(f"Area of Triangle is: {area_of_triangle}")

# Calculating the perimeter of a triangle
print("You are about to calculate the perimeter of a triangle")
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_of_triangle = side_a + side_b + side_c
print(f"Perimeter of Triangle is: {perimeter_of_triangle}")

# Calculating the area and perimeter of a rectangle
print("You are about to calculate the area and perimeter of a rectangle")
r_length = float(input("Enter the length: "))
r_width = float(input("Enter the width: "))
area_of_rectangle = r_length * r_width
perimeter_of_rectangle = 2 * (r_length + r_width)
print(f"Area of Rectangle is: {area_of_rectangle}")
print(f"Perimeter of Rectangle is: {perimeter_of_rectangle}")

# Calculating the area and circumference of a circle
print("You are about to calculate the area of a circle")
c_radius = float(input("Enter the radius: "))
area_of_circle = 3.14 * c_radius ** 2
circumf_of_circle = 2 * 3.14 * c_radius
print(f"Area of Circle is: {area_of_circle}")
print(f"Circumference of Circle is: {circumf_of_circle}")




# Compare length of characters
print("Length of 'python' is same with length of 'dragon': ", len("python") != len("dragon"))

Check if 'on' is in 'python' and 'dragon'
print("on is in python and dragon: ", "on" in "python" and "on" in "dragon")

Check if 'jargon' is in a sentence
print("If jargon is in 'I hope this course is not full of jargon': ", "jargon" in "I hope this course is not full of jargon")

Check if there is no 'on' in both 'dragon' and 'python'
print("'on' is not in 'python' and 'dragon': ", 'on' not in 'python' and 'dragon')

Find the length of 'python' and convert it to float and then to string
print(str(float(len('python'))))

# Check if a number is even
num = int(input("Enter a number: "))
print("Number entered is even: ", (num % 2) < 1)

# Check floor division
print("7 // 3 equals int(2.7):", 7 // 3 == int(2.7))

# Check if type of '10' == type 10
print("type('10') equals type(10):", type('10') == type(10))

Check if int('9.8') equals 10
print("int('9.8') equals 10:", int(9.8) == 10)

# Calculates weekly earnings
print("You are about to calculate employees weekly earnings")
hours = float(input("Enter number of hours: "))
rate_per_hr = float(input("Enter rate per hour: "))
weekly_earnings = hours * rate_per_hr
print(f"The employees weekly earning is: {weekly_earnings}")

