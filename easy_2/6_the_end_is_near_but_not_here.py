# PROBLEM
# Write a function that returns the next to last word in the string 
# argument.
# Words are any sequence of non-blank characters.
# You may assume that the input string will always contain at least two
# words.

# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# INPUTS
# A string

# OUTPUTS
# The word before the last in the string.

# RULES (explicit + implicit)
# Assume string input will always contain at least two words.
# Words = any sequence of non-blank characters
# Function can't accept empty strings.

# OBJECTS TO BE USED
# 

# PSEUDOCODE
# SET `return_word_before_last(string)`
#     SET `split_word_list` = `string` split into a list of words
#     RETURN second to last word in `split_word_list`

def return_word_before_last(string):
	split_word_list = string.split()
	return split_word_list[-2]

print(return_word_before_last("i loike it."))

# These examples should print True
print(return_word_before_last("last word") == "last")
print(return_word_before_last("Launch School is great!") == "is")


# SOLUTION
# Correct.
# First we split the words into a list of words.

# Anything that isn't whitespace is considered a word, so we can just
# use  `split` to divvy up the words. We then use negative indexing to
# get the next to last word in the list, which is at index `-2`.
