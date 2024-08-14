# PROBLEM
# Using the multiply function from the "Multiplying Two Numbers"
# exercise, write a function that computes the square of its argument 
# (the square is the result of multiplying a number by itself).

# EXAMPLES
# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# # MY SOLUTION
# def multiply(num1, num2):
# 	# print(num1, num2)
# 	return num1 * num2

# def square(num):
# 	# print(num)
# 	return multiply(num, num)

# print(square(7)) # 49

# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# SOLUTION
# Correct.

# Our solution relies on the previous exercise's `multiply` function.
# The return value of `multiply` is the result of multiplying the
# arguments together, so we just pass it the same number twice.
# The result is the squared value.

# FURTHER EXPLORATION
# Suppose we want to generalize this function to a "power to the n" 
# type function: cubed, to the 4th power, to the 5th, etc. How would we
# go about doing so while still using the multiply function?

# Not mine
def multiply(num1, num2):
    return num1 * num2

def power(base, exponent):
    result = 1
    for i in range(exponent):
        result = multiply(result, base)
        
    return result

print(power(3, 3)) # 27
print(power(2, 4)) # 16

# Result is set to `1`.
# It gets passed into the loop, so if `2` is the base & `4` the 
# exponent, `i` would be: 0, 1, 2, 3 
# `multiply(1, 4)` would be: `4`
# `4` gets reassigned to `result`
# Next loop
# `multiply(4, 4)` would be: `16`
# 