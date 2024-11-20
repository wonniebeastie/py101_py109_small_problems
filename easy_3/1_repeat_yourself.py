# PROBLEM
# Write a function that takes two arguments, a string and a positive 
# integer, then prints the string as many times as the integer 
# indicates.

# INPUTS
# 2 args - a string & a positive number

# OUTPUTS
# Printed - string as many times as the integer indicates.

# CLARIFYING QUESTIONS
# Does the integer need to be calidated as positive?

# CORE TASK
# Repeat a string an `n` number of times.

# KEY CONCEPTS
# Loops
# Function definition
# Function parameters
# String manipulation
# Function invocation
# Output

# PSEUDOCODE
# SET `repeat(string, num)`
#     IF `num` is positive, 
#         Assign that number to `counter`

#     WHILE `counter` is less than or equal to `num`,
#         PRINT `string`
#         Increment `counter` by 1

# MY SOLUTION
def repeat(string, num):
	if num > 0:
		counter = 0
	else:
		return print("Please enter a positive number.")
	
	while counter < num:
		print(string)
		counter += 1

repeat("I loike it", 3)

# SOLUTION 
def repeat(string, number):
    for _ in range(number):
        print(string)

# When solving exercises, it can be beneficial to progress in small 
# increments. We started out by defining repeat with two parameters. 
# Then, to ensure everything worked properly, we added a simple print
# statement inside the function:
def repeat(string, number):
    print(string)
# This works correctly, however, it only prints `string` once. Our goal 
# is to print string a specified number of times. To achieve this, we 
# use a `for` loop combined with the `range` function. This lets us execute
# the print statement any number of times as indicated by `number`.



# ------------ REVISIT ------------

def repeat(string, num):
	for _ in range(num):
		print(string)

repeat('Mucho', 6)


# ----------- OTHER STUDENT SOLUTIONS ----------

# 1
def repeat(str, num):
    print((str + '\n') * num)
# This code adds a new line to the end of the string argument and 
# multiplies it with `num` amount of times.

# This means that each repetition of the string will be followed by a
# line break when printed. 

# If `repeat('Hello', 2)` was used:
# `(str + '\n') * num` creates the string `'Hello\nHello\n'.
# And when you use the `print` function to print this, it prints:
# ```
# Hello
# Hello
#
# ```

# The `print` function adds a newline at the end of what it prints by
# default. 

# So I like the idea of this solution, but it doesn't achieve what the
# example output shows.


# 2
def repeat(string, multiple):
    counter = 1
    while counter <= multiple:
        print(string)
        counter += 1

# This solution does achieve what the example output shows.
# It is essentially the same as my previous one, but without
# the input validation for positive numbers.

# It sets the counter to `1` then uses a `while` loop to print
# the string until the number assigned to `counter` becomes
# larger than the input number passed as an argument.
