# PROBLEM
# Write a program that asks the user to enter an integer greater than 
# `0`, then asks whether the user wants to determine the sum or the 
# product of all numbers between `1` and the entered integer, inclusive.

# EXAMPLE 1
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

# EXAMPLE 2
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.

# INPUTS
# Integer > `0` from user input

# OUTPUTS
# Integer from user input
# `s` or `p`
# The sum of the integers between 1 and [chosen number] if input is `s`,
# OR
# The product of the integers between 1 and [chosen number] if input is
# `p`.

# RULES (explicit + implicit)
# Must ask user for an integer greater than `0`.
# This number must be outputted.
# Must ask user for sum or product of everything between `1` and 
# [chosen number].
# The result must be outputted.



# MY SOLUTION
def compute_sum(integer):
	return sum(range(1, integer + 1))

def compute_product(integer):
	product = 1
	for num in range(1, integer + 1):
		product *= num
	return product

while True:
	num = int(input('Please enter an integer greater than 0: \n'))
	if num <= 0:
		print('Please try again.')
	else:
		break

while True:
	sum_or_product = input(
		"Enter 's' to compute the sum, or 'p' to compute the product: \n"
		)
	if sum_or_product != 's' and sum_or_product != 'p':
		print(sum_or_product)
		print("Please try again")
	else: 
		break

if sum_or_product == 's':
	print(f'The sum of the integers between 1 and {num} is {compute_sum(num)}')
else:
	print(f'The product of the integers between 1 and {num} is {compute_product(num)}.')


# SOLUTION
def compute_sum(target_num):
    return sum(range(1, target_num+1))

def compute_product(target_num):
    result = 1
    for num in range(1, target_num+1):
        result *= num
    return result

prompt1 = "Please enter an integer greater than 0: "
prompt2 = ('Enter "s" to compute the sum, '
        'or "p" to compute the product: ')

number = int(input(prompt1))
operation = input(prompt2)
print()

if operation == "s":
    print("The sum of the integers between 1 and "
        f"{number} is {compute_sum(number)}.")
elif operation == "p":
    print("The product of the integers between 1 and "
        f"{number} is {compute_product(number)}.")
else:
    print("Oops. Unknown operation.")

# For brevity & simplicity, our solution doesn't try too hard to 
# validate the user input. 
# For completeness, your solution should try to validate input and
# issue error messages as needed.

# When using the `range` function, `target_num + 1` is used as the 
# second argument, since `range` excludes the end value.

# There is no equivalent to `sum` for computing products built-in to
# Python, so we have to do so ourselves.
# Note that the NumPy package does have a `prod` function, but NumPy
# is overkill for this exercise.

# FURTHER EXPLORATION
# Suppose the input was a list of space separated integers instead of 
# just a single integer? 
# How would your `compute_sum` and `compute_product` functions change?