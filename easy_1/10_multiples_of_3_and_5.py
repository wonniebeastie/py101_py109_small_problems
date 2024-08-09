# PROBLEM
# Write a function that computes the sum of all numbers between 1 and
# some other number, inclusive, that are multiples of 3 or 5. 
# For instance, if the supplied number is 20, the result should be 
# 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.


# INPUTS
# A given integer

# OUTPUTS
# The sum of all numbers of the given input that are multiples of 3 & 5

# RULES (explicit + implicit)
# No repeats (shown in example)
# Given number is > 1 
# Given number must be included 

# MENTAL MODEL
# Given a number, write a function that will add up all the numbers 
# between that number (inclusive) 

# OBJECTS TO BE USED
#

# PSEUDOCODE
# n % 3 == 0
# n % 5 == 0

def multisum(number):
	# print(number) Am I getting the correct value?
	total = 0
	for num in range(number + 1):
		# print(num) Are the elements in the range what I want?
		if num % 3 == 0 or num % 5 == 0:
			# print(num)
			# print(total) see total BEFORE it's added
			total += num
			# print(total) see total AFTER it's added
		# print(f"Current number: {num} Current total:{total}")
	return total

print(multisum(10))   # 33


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)


# SOLUTION
def is_multiple(number, divisor):
    return number % divisor == 0

def multisum(max_value):
    total_sum = 0
    for number in range(1, max_value + 1):
        if is_multiple(number, 3) or is_multiple(number, 5):
            total_sum += number
    return total_sum

# Extra `is_multiple` function returns `True` if the given number is 
# a multiple of the divisor, or `False` if it is not.
# This function isn't entirely necessary but it makes the main function
# more readable.

# The main function, `multisum`, adds each appropriate value in the 
# range to our `sum` variable.