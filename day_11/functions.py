# Day 11 of 30 days of python

# # Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# def add_two_numbers(x, y):
#     total = x + y
#     return total
# print("Sum of 4 and 8 is: ", add_two_numbers(4, 8))

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# def area_of_circle(radius):
#     pi = 3.14
#     area = pi * radius * radius
#     return area
# print("The area of a circle is", area_of_circle(3))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
numbers_to_add = int(input("How many numbers do you want to add? "))
list_item = []
while numbers_to_add > 0:
    try:
        num = float(input("Input number: "))
        numbers_to_add -= 1
        list_item.append(num)
    except ValueError:
        print("Only numbers are accepted")
        break

# print(list_item)

items_str = ', '.join(str(item) for item in list_item)
def add_all_nums(*nums):
    total = 0
    for n in nums:
        total += n
    return total
print(f"The sum of {items_str} is: ", add_all_nums(*list_item))
    
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# Write a function called calculate_slope which return the slope of a linear equation
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list