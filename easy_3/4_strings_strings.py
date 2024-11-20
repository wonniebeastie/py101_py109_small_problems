# PROBLEM
# Write a function that takes one argument, a positive integer, and 
# returns a string of alternating '1's and '0's, always starting with 
# a '1'. The length of the string should match the given integer.

# GOAL
# To write a function that takes a positive integer & returns a string 
# of alternating '1's & '0's with the length that matches the input.

# INPUTS & OUTPUTS
# I: A positive integer
# O: A string of alternating `1`s & `0`s the length of the string

# EXAMPLE(S)
# I: 6
# O: "101010"

# I: 4
# O: "1010"

# RULES (EXPLICIT/IMPLICIT)
# - Input must be a positive number.
# - Output must start with `'1'`
# - Length of the string should match the given integer.

# BRAINSTORM
# Loop - runs for the length of the input
# String multiplication
# `'1'` should be index 0 (then the rest of the even indexes)
# `'0'` should be index 1 (then the rest of the odd indexes)
# range?

# STEPS
# Define function `stringy` (Takes one argument = a positive integer `num`)
#      SET `binary` = ""
#
#      If `num` is < `1`,
#          return `binary`
#
#      For each `number` in range of `0` - `num`:
#          If `number` is odd, concatenate `'1'` to `binary`
#          Else concatenate `'0'` to `binary`

def stringy(num):
	binary = ''

	if num < 1:
		return binary
	
	for number in range(num):
		if number % 2 == 0:
			binary += '1'
		else:
			binary += '0'
	
	return binary



print(stringy(4))
print(stringy(2))
print(stringy(5))

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True


# SOLUTION

def stringy(size):
    result = ""
    for idx in range(size):
        digit = '1' if idx % 2 == 0 else '0'
        result += digit

    return result

# The solution makes use of a for loop in combination with range to 
# loop the specified number of times. At every iteration of the loop, 
# the solution checks whether the index position is even. If so, the 
# solution appends a '1' to the initially empty result string. 
# Otherwise, it appends '0'.

# This ternary expression:
number = '1' if idx % 2 == 0 else '0'

# is equivalent to using an if/else statement:
if idx % 2 == 0:
    number = '1'
else:
    number = '0'


# OTHER STUDENT SOLUTIONS

# 1
def stringy(size):
    return '10' * (size // 2) + '1' * (size % 2)

# This solution has a function that will:
# 1) divide the input by 2, but rounded down to the nearest whole number, 
# 2) multiply the result with the string `'10'` 
# (Step 1 determines how many times the string `'10'` will be repeated),
# 3) find the modulus of the input & 2,
# 4) multiply the result with the string `'1'` if modulus is `1`
#    do nothing if moulus is `0`.

# For size = 6:
# '10' * (6 // 2) → '101010'
# '1' * (6 % 2) → '1' * 0 → '' (nothing added)
# '101010'

# For size = 7:
# '10' * (7 // 2) → '101010'
# '1' * (7 % 2) → '1' * 1 → '1'
# '1010101'

# 2
def stringy(length):
    return ''.join(['1' if i % 2 == 0 else '0' for i in range(length)])

# This solution creates a list with a list comprehension -
# List comprehension:
# → The ternary expression '1' if i % 2 == 0 else '0' is the expression.
#      - If i is even (i % 2 == 0), it returns '1'
#      - If i is odd, it returns '0'

# → For each element in range(length)

# After list comprehension:
# → This returns a list with either '1's added for even indexes, or '0's
#   added for odd indexes:
#     - Example: For length = 5, the list will be ['1', '0', '1', '0', '1'].

# → Then joins them together into a string using the string method 
# .join(), which takes all items in an iterable and joins them into a string.