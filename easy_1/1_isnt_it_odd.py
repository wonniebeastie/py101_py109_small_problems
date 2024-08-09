# Write a function that takes one integer argument and returns True 
# when the number's absolute value is odd, False otherwise.


# STEP 1: UNDERSTAND THE PROBLEM

# INPUTS
# One integer

# OUTPUTS
# True if input's absolute value is odd, False otherwise.

# RULES
# One integer argument
# Find the absolute value of argument first 
# (Absolute Value - a number's distance from zero along the real number
# line. Or the modulus of a real number.)
# Then check if the AV is an odd number or an even number.


# STEP 2: EXAMPLES

# TEST
# Input: 4
# Output: False

# Input: -9
# Output: True


# STEP 3/4: DATA STRUCTURE/ALGORITHM

# IN PLAIN ENGLISH
# Given an integer
#     Find the absolute value of the integer.
#     If the AV is an odd number,
#         Return True
#     Otherwise, return False.

# FORMALIZE PSEUDOCODE

# Given an integer 

# FUNCTION check_av_odd_or_even(integer)
#     SET integer =  absolute value of integer
#     IF integer = number % 2 is NOT 0,
#         RETURN True
#     ELSE
#         RETURN False


# STEP 5: CODE

# MY SOLUTION
def check_av_odd_or_even(integer):
    integer = abs(integer)
    if integer % 2 != 0:
        return True
    else:
        return False

print(check_av_odd_or_even(-356))







# SOLUTION
def is_odd(number):
    return abs(number) % 2 == 1
# The abs function returns the absolute value of the argument, ensuring 
# it's positive. 
# We then check whether the resulting number modulo 2 equals 1, which 
# would indicate it's odd.

# It's actually not necessary to use `abs` here; when evaluating 
# `n % d` where `n` is an integer and `d` is `1`, `-1`, or `2`, it 
# doesn't matter whether `n` is positive or negative. 
# However, if `d` isn't `1`, `-1`, or `2`, it does matter. 
# To make the code as clear as possible, using `abs` is a good idea.