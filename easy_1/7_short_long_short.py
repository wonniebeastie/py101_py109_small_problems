# PROBLEM
# Write a function that takes two strings as arguments, determines the 
# length of the two strings, and then returns the result of 
# concatenating the shorter string, the longer string, and the shorter
# string once again. 
# You may assume that the strings are of different lengths.

# EXAMPLE
# # These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")


# INPUTS
# Two strings

# OUTPUTS
# A single string: the shorter string + longer string + shorter string

# RULES (explicit + implicit)
# Determine the length of the two strings
# Strings are of different lengths


# PSEUDOCODE
# SET `short_long_short(string1, string2)`:
#     IF len(string1) < len(string2):
#         PRINT string1 + string2 + string1
#     ELSE
#         PRINT string2 + string1 + string2


# MY SOLUTION
def short_long_short(string1, string2):
	if len(string1) < len(string2):
		return string1 + string2 + string1
	else:
		return string2 + string1 + string2

print(short_long_short('ice', 'mans')) # icemansice

print(short_long_short('abc', 'defgh') == "abcdefghabc") # True
print(short_long_short('abcde', 'fgh') == "fghabcdefgh") # True
print(short_long_short('', 'xyz') == "xyz") # True 

# At first, I did this: 

# def short_long_short(string1, string2):
# 	if len(string1) < len(string2):
# 		print(string1 + string2 + string1)
# 	else:
# 		print(string2 + string1 + string2)

# short_long_short('ice', 'mans') # icemansice

# print(short_long_short('abc', 'defgh') == "abcdefghabc") # False
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh") # False
# print(short_long_short('', 'xyz') == "xyz") # False

# Then I realized it was returning False because the `print()` function 
# outputs text to the console but returns `None`.


# SOLUTION
# Correct.
