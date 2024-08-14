# PROBLEM
# Write a function that takes a number as an argument. If the argument 
# is a positive number, return the negative of that number. If the 
# argument is a negative number, return it as-is.

# INPUTS
# A number

# OUTPUTS
# If input is positive, return the negative
# If number is negative, return as-is

# MY SOLUTION
def negative(num):
	if num > 0:
		return -num
	else:
		return num

print(negative(99))
print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True


# SOLUTION
def negative(number):
    return -abs(number)

# Python has a built-in `abs()` function which returns the absolute
# value of a specified number. By prefixing the result of abs(number) 
# with a negative sign -, the function effectively always returns the 
# negative representation of the given number.