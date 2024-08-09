# PROBLEM
# Write a function that determines and returns the UTF-16 string value 
# of a string passed in as an argument. 
# The UTF-16 string value is the sum of the UTF-16 values of every 
# character in the string. 
# (You may use `ord` to determine the UTF-16 value of a character.)

# INPUTS
# A string

# OUTPUTS
# the UTF-16 string value of the input string

# RULES (explicit + implicit)
# UTF-16 str value = sum of the UTF-16 values of every char in the string
# `ord` may be used to determine the UTF-16 value of a char.

# OBJECTS TO BE USED
#

# PSEUDOCODE
# SET `utf16_value(string)`:
#     `unicode` = ord(`string`)
#     `unicode` = Turn code into a list of values
#      FOR each value of the list `unicode`
#           Add to the previous one
#         
#      Return result

# import pdb

# MY SOLUTION
def utf16_value(string):
	# print(string) so I know what I wanted was passed in.
	total = 0 # ALWAYS OUTSIDE for loop or else loop will keep resetting to 0 if you put it inside the loop.
	for char in string:
		# print(char) so I know which character is being worked on.
		# print(ord(char))
		total += ord(char)
		# print(total)
	return total

print(utf16_value('hello')) # 532

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)


# SOLUTION
def utf16_value(string):
    sum_ = 0
    for char in string:
        sum_ += ord(char)
    return sum_

# The variable was named with an underscore suffix - `sum_` - to avoid
# shadowing Python's built-in `sum` function. 

# The function iterates through each character in the given string 
# using a `for` loop. 
# For each character, we use the `ord` function to get its UTF-16 value
# & add it to the sum.
# Finally, after iterating through all the characters, the function 
# returns the sum of all the character values.