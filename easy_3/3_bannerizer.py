# PROBLEM
# Write a function that takes a short line of text and prints it within a box.

# GOAL
# To write a function that takes text and prints it within a box.

# INPUTS & OUTPUTS
# I: a string
# O: the input string in a box

# EXAMPLE(S)
# I: 'To boldly go where no one has gone before.'
# O:
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

# I: ''
# O: 
# +--+
# |  |
# |  |
# |  |
# +--+

# RULES (EXPLICIT/IMPLICIT)
# - Assume output will always fit in terminal window.
# - Empty string should still print a box.

# QUESTIONS / BRAINSTORM
# - The entire thing is 5 lines long.
# - Width depends on how long the input text is.
#
# Lines 1 & 5
# - First part should start with `+-`
# - Last part should end with `-+`
# - Middle should be padded with `-` for however long
# the input text will be. 
#
# Lines 2 & 4
# - Starts with `| `
# - Middle is whitespace for however long the input text will be.
# - Ends with ` |`
#
# Line 3
# - Starts with `| `
# - Middle is for input text.
# - Ends with ` |`

# STEPS
# Define function `print_in_box` (Takes one text argument `txt`)
#      SET `txt_length` variable with length of argument string.
#      Print `'+-'` + dashes as long as length of `txt` + `'-+'`
#      Print `'| '` + whitespace as long as length of `txt` + `' |'`
#      Print `'| [txt] |'` (embed `txt` into string)
#      Print `'| '` + whitespace as long as length of `txt` + `' |'`
#      Print `'+-'` + dashes as long as length of `txt` + `'-+'`

def print_in_box(txt):
	txt_length = len(txt)

	print(f"+-{'-' * txt_length}-+")
	print(f"| {' ' * txt_length} |")
	print(f"| {txt} |")
	print(f"| {' ' * txt_length} |")
	print(f"+-{'-' * txt_length}-+")

print_in_box('I loike it.')

# +-------------+
# |             |
# | I loike it. |
# |             |
# +-------------+


# SOLUTION
def print_in_box(message):
    horizontal_rule = f'+-{"-" * len(message)}-+'
    empty_line = f'| {" " * len(message)} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)

# This is a fairly straight forward solution. We use Python's built-in 
# string multiplication to generate the horizontal rules and the spaces 
# required for the box.

# The tricky part of this solution is getting the horizontal rule and 
# empty line formatting strings correct. With the rule, we start by 
# constructing a string that contains len(message) + 4 characters, most 
# of which are hyphens (-). We bound the line with a + character at 
# either end. We do something similar with the empty lines above and 
# below the message, but this time we use spaces instead of hyphens, 
# and | characters instead of + characters.

# We could have written both strings a little differently:
horizontal_rule = f'+{"-" * (len(message) + 2)}-+'
empty_line = f'|{" " * (len(message) + 2)}|'


# However, we opted for what we felt were more readable strings.

# In Python, the * operator is used for multiplication when working 
# with numbers. However, when used with strings, it repeats a string 
# a given number of times.

# Let's analyze this line from our first solution:
horizontal_rule = f'+-{"-" * len(message)}-+'

# 1. len(message) returns the length of the message we want to print.

# 2. "-" * len(message) returns a string of N hyphens, where N is the 
# the length of the message we want to print.

# 3. We then prepend +- to the beginning of the hyphens.

# 4. Finally, we append -+ to the end of the hyphens.

