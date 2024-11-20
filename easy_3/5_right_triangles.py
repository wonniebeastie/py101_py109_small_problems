# PROBLEM
# Write a function that takes a positive integer, n, as an argument and
# prints a right triangle whose sides each have n stars. The hypotenuse 
# of the triangle (the diagonal side in the images below) should have 
# one end at the lower-left of the triangle, and the other end at the 
# upper-right.

# INPUTS & OUTPUTS
# I: positive integer `n`
# O: printed right triangle whose sides each have `n` stars

# EXAMPLE(S)
# I: 5
# O:
#     *
#    **
#   ***
#  ****
# *****

# RULES (EXPLICIT/IMPLICIT)
# - Input has to be a positive integer.
# - Outputted triangle must be a right triangle (one end of the 
#   hypotenuse should have one at the lower-left and one at the upper
#   -right).

# QUESTIONS / BRAINSTORM
# - Each row has spaces & stars.
# - Since the bottom, being a side, also has the number of stars that
#   match the input #, and each row above has one less, maybe loop from
#   1 star til there are `n` amount of stars
# - maybe replace each space with a star * for each row: `n + 1`

# DS
# for loop

# STEPS
# Define function `triangle` (takes one argument `n`)
#     row_num = `n`
#     star_num = 1
#
#     for each row in a range of 1 ~ `n`
#         print whitespace `row_num - 1` number of times + `star_num`
#         `row_num`-= 1
#         `star_num` += 1


# My solution 1 
def triangle(n):
	row_num = n
	star_num = 1

	for row in range(n):
		print(f'{" " * (row_num - 1)}{"*" * star_num}')
		row_num -= 1
		star_num += 1

triangle(5)
#     *
#    **
#   ***
#  ****
# *****

# Pros:
# - Clear logic, manually track spaces & stars.
# - Easy to understand because the values are incremented & decremented
#   explicitly.

# What can be improved:
# - Use `range(n, n + 1)` for more human-readable code.
# - `row_num` & `star_num` don't really need to be tracked since they 
#    always increase and decrease together; You can simplify the logic
#    by only using `row` index from the loop:

# def triangle(n):
#     for row in range(n):
#         print(f'{" " * (n - row - 1)}{"*" * (row + 1)}')



# My solution 2
def triangle_2(n):
	space = ' ' * n
	each_time = 1

	for row in range(n):
		whoa = space.replace(' ', '*', each_time)
		print(whoa[::-1])
		each_time += 1

triangle_2(8)
#        *
#       **
#      ***
#     ****
#    *****
#   ******
#  *******
# ********




# SOLUTION
def triangle(height):
    for num in range(1, height + 1):
        spaces = height - num
        stars = num
        print(f'{" " * spaces}{"*" * stars}')

# For this problem, we use a loop with the range function to iterate 
# from `1` to `height`, inclusive. This helps us determine the number 
# of stars to print in each line.

# In each iteration of the loop:

# -> We determine the number of spaces to be printed as `height - num`. 
#    As `num` increases, the number of spaces decreases.

# -> We determine the number of stars to be printed as `num`. As `num` 
# increases, the number of stars increases.

# As mentioned in one of the previous problems, Python's string 
# multiplication (*) is used to create a string with a repeated sequence
# of characters. This lets us generate the appropriate number of spaces 
# and stars for each line of the triangle.


# OTHER STUDENT SOLUTIONS

# 1
def triangle(n):
    for i in range(1, n + 1):
        stars = "*" * i
        print(stars.rjust(n))
# This one uses the `.rjust()` string method. This method right aligns
# the string, using a space (default) or a specified character to fill
# the left side with. 

# So for each number in range from 1 to n + 1,
#     `stars` = "*" * each number in range
#     Print `stars` with `.rjust()`, making the stars right-align while
#     filling the left side with whitespaces.

# 2
def triangle(num):
    for i in range(1, num + 1):
        print((' ' * (num - i)) + ('*' * i))
# For this one:
# - For each number in range of 1 to n + 1,
# -     Print (' ' * (n - each number)) + ('*' * each number)