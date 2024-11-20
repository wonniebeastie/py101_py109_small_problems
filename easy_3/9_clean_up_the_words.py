# PROBLEM
# Given a string that consists of some words and an assortment of 
# non-alphabetic characters, write a function that returns that string 
# with all of the non-alphabetic characters replaced by spaces. If one 
# or more non-alphabetic characters occur in a row, you should only 
# have one space in the result (i.e., the result string should never 
# have consecutive spaces).

# INPUTS & OUTPUTS
# I: A string with words & non-alphabetic characters
# O: The input string with the non-alphabetic chars replaced with spaces

# EXAMPLE(S)
# I: "---what's my +*& line?"
# O: " what s my line "

# RULES (EXPLICIT/IMPLICIT)
# - All non-alphabetic chars should be replaced with a single space.
# - Any consecutively-occuring non-alphabetic chars should be replaced
#   by only one space.
# - Leading and trailing spaces are allowed.

# QUESTIONS / BRAINSTORM
# - Split string into list of characters.
# - Iterate through the list:
#    - Identify if each one is:
#       - A letter
#       - A whitespace
# - Add character to new list if either of the above & previous char
#   is not a space.
# - If it is a special character, replace with `' '`.
#    - However, if the character added last is a space, skip this step.

# GOAL
# To write a function that replaces the special chars in a string with 
# only one space and returns it. 

# DS
# for loop
# list

# STEPS
# Define function `clean_up` (takes single line of text as argument `txt`)
#   SET `split_txt` variable with `txt` split into a list of characters.
#   SET `new_list` with an empty list.
#
#
#   Iterate through `split_txt` using a loop
#     Check if character is a letter or a whitespace.
#     If either of those are true AND the previous char is not a space,
#        add it to `new_list`.
#     If the character is a special char AND the previous char is not a space,
#        add `' '` to `new_list`.
#
#    Return `new_list`

def clean_up(txt):
	split_into_chars = list(txt)
	new_list = []
	prev_value_special = False
	for char in split_into_chars:
		if char.isalpha():
			print(f"Is letter:{char}")
			new_list.append(char)
			prev_value_special = False

		else:
			print(f"not letter: {char}")
			if not prev_value_special:
				new_list.append(" ")
				prev_value_special = True
	new_list = ''.join(new_list)
	print(f"New List: {repr(new_list)}")
clean_up("---what's my +*& line?")
# print(clean_up("---what's my +*& line?") == " what s my line ")
# True



# def clean_up(txt):
# 	split_txt = list(txt)
# 	print(split_txt)
# 	new_list = []
# 	prev_char = ""

# 	for char in split_txt:
# 		print(f'char: {repr(char)}')
# 		if not char.isalpha() and prev_char != " ":
# 			new_list.append(' ')
# 			print(f"new_list so far: {new_list}")
# 		elif char.isalpha():
# 			new_list.append(char)
# 			print(f"new_list so far: {new_list}")
# 		prev_char = new_list[-1]

# 	new_txt = ''.join(new_list)

# 	return repr(new_txt)