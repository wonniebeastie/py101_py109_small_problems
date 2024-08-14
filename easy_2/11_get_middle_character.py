# PROBLEM
# Write a function that takes a non-empty string argument and returns 
# the middle character(s) of the string. If the string has an odd 
# length, you should return exactly one character. If the string has an
# even length, you should return exactly two characters.

# CORE TASK
# Finding the middle character(s) of a string

# INPUTS
# Non-empty string

# OUTPUTS
# The middle character of the string

# RULES (explicit + implicit)
# Odd & Even lengths require different ways of handling:
# String has an odd length - return exactly one character
# String has an even length - return exactly two characters

# KEY CONCEPTS
# `0`-based indexing in Python
# Floor Division `//`
# Odd vs Even using the Modulo operator `%`
# String slicing

# PSEUDOCODE
# SET function `center_of(string)`
#     Get length of string & assign it to variable `string_length`
#     SET variable `midpoint` = Half the length of string, rounded down
#
#     IF `string_length` is odd,
#          RETURN 1 character from `string` using `midpoint` as the index #
#     ELSE
#          RETURN 2 characters - one same as above & the one left of it 

def center_of(string):
	string_length = len(string)
	midpoint = string_length // 2

	if string_length % 2 != 0:
		return string[midpoint]
	else:
		return string[midpoint - 1: midpoint + 1] # Stop value is exclusive

# The point for even lengths is to get the char on the left of the
# middle point by -1 bc of zero-based indexing Python uses 

print(center_of("word")) # or

# SOLUTION
def center_of(string):
    if len(string) % 2 == 1:
        center_index = len(string) // 2
        return string[center_index]
    else:
        left_index = len(string) // 2 - 1
        return string[left_index:left_index + 2]
    
# Main difficulty comes from understanding the indexes you're working
# with. When an indexing problem is complex, walk through one or two
# examples so you can wrap your head around what needs to be done. 

# 5-CHAR STRING
# string	T	u	r	b	o
# index	    0   1   2   3	4
# center			*		

# Testing with a string of length 5 & length 7 shows a pattern of 
# dividing the string length by half, rounded down, is the middle char.

# length	center index
#   5	     5 // 2 => 2
#   7	     7 // 2 => 3
#   3	     3 // 2 => 1

# Then we can generalize the pattern: 

# ODD NUMBERS
# If `n` is an odd number & you 
# have a string length of `n`, then the middle char is at: 
# index `n // 2`.
# So we just need to get the character at that index (`string[5 // 2]`) 
# for a 5-character string.

# `/` returns a FLOAT.
# Since we want an integer, we use integer division `//` instead.
# Integer division, when working with positive integers, discards any
# remainder & gives the result as an integer. (`//`'s behavior is more
# complicated when dealing with floats & negative numbers but it's not
# relevant here.)

# EVEN NUMBERS
# 6-CHAR STRING
# string	s	u	b	w	a	y
# index	    0	1	2	3	4	5
# center			*	*		

# Same pattern as odd numbers, but we see that the character to the left
# of that is also in the middle. If we repeat this with a 8-char string,
# the indexes would be `3` & `4`. 

# A 4-char string would be indexes `1` & `2`.

# length   right index	  left index
#   6	   6 // 2 => 3	  3 - 1 => 2
#   8	   8 // 2 => 4	  4 - 1 => 3
#   4	   4 // 2 => 2	  2 - 1 => 1

# Again there's a pattern. Now we can use string slicing to get the
# characters. `string[left_index:left_index + 2]` will extract 2 chars
# from the string starting at left_index.