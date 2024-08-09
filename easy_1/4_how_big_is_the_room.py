# PROBLEM
# Build a program that asks the user to enter the length and width of 
# a room, in meters, then prints the room's area in both square meters 
# and square feet.

# Note: 1 square meter == 10.7639 square feet

# INPUTS
# User input: length of a room (meters)
# User input: width of a room (meters)

# OUTPUTS
# The room's area in square meters
# The room's area in square feet

# RULES (explicit + implicit)
# Length & width must come from user input.
# The room's area must be printed in both square meters & square feet.
# The square feet can be converted from the square meter.

# OBJECTS TO BE USED
# 

# PSEUDOCODE


# SET `print_room_area(length, width)`:
#   SET `length` = GET from user: 'What is the room's length in meters?: '
#   SET `width` = GET from user: 'What is the room's width in meters?: '
#   
#   SET `area` = length * width

#   PRINT 'The room is (`area`) square meters and (`area` * 10.7639) square feet.'


# MY SOLUTION
def print_room_area():
    length = int(input('What is the room\'s length in meters?: '))
    width = int(input('What is the room\'s width in meteres?: '))

    area = length * width

    print(f'The room is {area} square meters and {area * 10.7639} square feet.')

print_room_area()


# SOLUTION
length = float(input("Enter the length of the room in meters: "))
width = float(input("Enter the width of the room in meters: "))

area_in_meters = length * width
area_in_feet = area_in_meters * 10.7639

print(f"The area of the room is {area_in_meters:.2f} "
    f"square meters ({area_in_feet:.2f} square feet).")
# The program first collects input values from the `length` and `width` 
# of a room, performs the computations to determine the area, then
# displays the results. 
# The solution does not check for invalid user input.

# Key things to note:
# - The `input` function returns a string. Thus, we need to use the 
# `float` function to convert this string to a floating-point number.
# - The format specification `{:.2f}` ensures that the output is 
# formatted to two decimal places.

# FURTHER EXPLORATION
# Modify the program to let the user specify the measurement type 
# (meters or feet). 
# Compute the area accordingly and print it and its conversion in 
# parentheses.