# PROBLEM
# A double number is an even-length number whose left-side digits are
# exactly the same as its right-side digits. For example, 44, 3333, 
# 103103, and 7676 are all double numbers, whereas 444, 334433, and 107
# are not.

# Write a function that returns the number provided as an argument 
# multiplied by two, unless the argument is a double number. If the 
# argument is a double number, return the double number as-is.

# INPUTS & OUTPUTS
# I: a number
# O: the number * 2 or the number if it's a double number

# EXAMPLE(S)
# I: 37
# O: 74

# I: 334433
# O: 668866

# I: 7676
# O: 7676

# RULES (EXPLICIT/IMPLICIT)
# - Double number: 
#    - Even length
#    - Left side digits are exactly the same as right side digits.
# - Number should be returned as is if it's a double number.
# - Result of multiplying inputted number with 2 should be returned
#   if it isn't a double number.

# QUESTIONS / BRAINSTORM
# - Since it's the argument that must be determined if it's a double 
#   number or not, it should be checked first to see if it is.
# - If it is, return it,
# - If it isn't, multiply by two, return the result.
# - How to check?
#    - check if it's even (so odd numbers are automatically multiplied)
#    - find the length of integer, divide down the middle 
#        - check if left side matches the right side
#        - if match, return the number
#        - else, multiply by two and return the result
# - Integers aren't sequences so they gotta be converted to strings to be
#   compared. 
# - Once converted, find the length of the string. `str_length`
# - Split it evenly down the middle - use slicing? 
#    - slicing - use the resulting # from `str_length`?
# - Compare the two sides 

# STEPS
# Define function `twice` (takes `num` as argument)
#     Convert `num` into text - SET `num_as_str`
#     Store length of `num_as_str` into variable SET `str_length`
#     
#     If `str_length` is an odd number, multiply by 2, return result.
#
#     Divide `str_length` by half. Store this - SET `half_length`
#
#     Does first half of `num_as_str` equal in value to second half of it?
#     If yes, convert it to an integer again and return it.
#     Else, convert it to an an integer again, multiply it by 2, 
#        then return it.

def twice(num):
	num_as_str = str(num)
	str_length = len(num_as_str)

	if str_length % 2 != 0:
		return num * 2
	
	half_length = int(str_length / 2)

	match = num_as_str[:half_length] == num_as_str[half_length:]
	if match == True:
		return num
	else:
		return num * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True


# Notes:
# - I forgot I could use floor division to get an integer intead of
#   coercing it with an `int()` constructor.



# SOLUTION

def is_double_number(number):
    string_number = str(number)
    center = len(string_number) // 2
    left_number = string_number[:center]
    right_number = string_number[center:]

    return left_number == right_number

def twice(number):
    if is_double_number(number):
        return number
    else:
        return number * 2

# The logic for checking whether a number is a "double number" is 
# maintained in the `is_double_number` function. Python's string slicing
# capabilities make it straightforward to compare the left half of the 
# number to the right half.

# - We convert the number into a string using the `str` function.

# - Next, we find the midpoint (or center) of the string. We use 
#   integer division (`//`) to ensure we get an integer result.

# - We then split the string into `left_number` and `right_number` 
# using Python's slicing syntax.

# - Finally, we check whether the left and right halves are equal and
#   return the result.

# The main function `twice` simply checks if the number is a "double 
# number" and, depending on the result, either returns the number itself
# or its doubled value.


# OTHER STUDENT SOLUTIONS
def twice(num):
    dd = str(num)
    half = len(dd) // 2

    return num * 2 if dd[:half] != dd[half:] else num
# This solution coerces `num` into a string -> stores it in `dd`
# Divides the length of the string by 2 -> stores it in `half`
# 
# Then uses a ternary expression:
# (<expression to return if condition is true> if <condition> <expression to return if condition is false>)
# <num * 2> if <dd[:half] != dd[half:] else <num>

# So this translates to: 
# Return `num * 2` if the first half of the string `dd` does NOT match 
# the second half of the string `dd`, and return `num` if it does. 