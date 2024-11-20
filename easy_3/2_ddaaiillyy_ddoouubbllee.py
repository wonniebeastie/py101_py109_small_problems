# PROBLEM
# Write a function that takes a string argument and returns a new 
# string that contains the value of the original string with all 
# consecutive duplicate characters collapsed into a single character.

# EXAMPLES
# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# INPUTS
# A string

# OUTPUTS
# Returns a new string with repeat chars of the OG string collapsed 
# into single chars.

# RULES (explicit + implicit)
# - Input string can be empty
# - Non-consecutive repeat chars are allowed.
# - String must be returned, not printed.

# CORE TASK
# Collapse consecutive repeat characters in a string into single chars.

# SUB-TASKS
# Decide how to iterate through the characters of the string.
# Figure out how to determine that a character repeats itself consecutively.
# Figure out a way to collapse them into a single character.
# Figure out how to put it all together to return it as a new string.

# KEY CONCEPTS
# 

# PSEUDOCODE
# Create function `crunch` that takes `str` as an argument.
#     Iterate over each character in `str`, 
#         Check if the character that comes after it is the same 
#         If it is NOT the same, add it to the new string,
#            then go onto the next char.
#         If it IS the same, 
#             find out how many times it repeats and skip over them all
#             until a character that is NOT the same is encountered.
#     Return the new string.




# ------------ REVISIT ----------------

# GOAL
# To write a function that takes a string and returns it with repeat
# consecutive chars collapsed into 1 char.

# INPUTS & OUTPUTS
# I: a string
# O: new string 

# EXAMPLE(S)
# I: 'ddaaiillyy ddoouubbllee'
# O: 'daily double'

# I: 'ggggggggggggggg'
# O: 'g'

# I: 'a'
# O: 'a'

# I: ''
# O: ''

# RULES (EXPLICIT/IMPLICIT)
# - Argument must be a string.
# - Returned string must have all consecutive duplicate chars collapsed
# into a single char.
# - If no duplicates, return as is.
# - Numbers must also be treated the same as the letters.

# QUESTIONS / BRAINSTORM
# - Sets might be one way - being collection of unique objects
# 	But sets are unordered.
# - Splitting string into a list of chars? Then checking if the char 
# already exists in the list, if it doesn't add to new list, if it does,
# then skip.  <- The problem with this is that it will check the entire 
# list, so it won't be checking for consecutive chars.
# - Iterate through characters in string, check if current char matches
# previous char, and if it does, don't add it to list, if it doesn't, add
# to new list. Then concatenate it into a string and return. 

# STEPS - High Level
# 1. If nothing in "container", first char auto-add
# 2. Then, first char compared to 2nd char
# 3. If 2nd char matches to first char, skip & continue
# 4. If no match, add it to "container"
# 5. Repeat until end of og object
# 6. Return new object 

# DS 
# while loop
# strings


def crunch(str):
	# Return string as is if empty.
	if str:
		container = str[0]
	else:
		return str
	
	index = 1
	# Check if previous char matches current char.
	while index < len(str):
		# If the previous char matches, just increment `index`
		if str[index-1] == str[index]:
			index += 1
		# Otherwise, concatenate character to existing string (`container`)
		else:
			container += str[index]
			index += 1
	
	return container

print(crunch('hnnnnngggh')) # hngh
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')  # True
print(crunch('4444abcabccba') == '4abcabcba')  # True
print(crunch('ggggggggggggggg') == 'g')  # True
print(crunch('abc') == 'abc')  # True
print(crunch('a') == 'a')  # True
print(crunch('') == '')  # True


# SOLUTION
def crunch(text):
    index = 0
    crunched_text = ''

    while index < len(text):
        if index == len(text) - 1 or text[index] != text[index + 1]:
            crunched_text += text[index]
		
        index += 1
	
    return crunched_text

# Solution builds a string named `crunched_text` by iterating over the
# chars in the `text` argument. While iterating, we append the character
# at the current index to `crunched_text` if the character is not equal
# to the next character. 

# If it is equal, then do nothing. 


# NOTES
# LS's solution differs from mine that:
# - It does not check whether the string is empty first.
# - It starts from index `0`.
# - Mine compares each character to the previous one (`str[index-1]`), 
#   while
#   LS's compares each character to the next one (`text[index + 1]`).
# - Mind handles the last character implicitly, 
#   while
#   Ls's handles it explicitly (`index == len(text) - 1`).
# - Mine repeats the code to incrementat `index` in both cases 
#   while
#   LS's does it only once.


# -------- OTHER STUDENT SOLUTIONS ----------

#1 
def crunch(text: str):
    crunched = ""
    for char in text:
        if not crunched.endswith(char):
            crunched += char
    return crunched
# This one uses a "type hint" for  documentation purposes.

# The `endswith()` method returns `True` if the string ends with the
# specified value, otherwise, `False`.

# So if the method returns `True` in that the last character currently
# assigned to `crunched` matches the current character in the iteration
# of `text`, it is flipped to `False`. So since this makes the `if` 
# condition falsy, it does not execute its body and goes onto the next
# iteration.

# If the method returns `False` in that the last character currently 
# assigned to `crunched` does NOT match the `char` in that iteration, 
# the `not` operator flips it to `True`, making the `if` condition 
# truthy, causing the body to execute and concatenate that character
# to what's currently assigned to `crunched`. 

# I like this because it's very concise & elegant. It's good to be 
# aware of such methods, but at this point in my learning journey,
# I think I should focus on how to code using just the very basics.


# 2
def crunch(string):
    if not string:
        return string
    
    result = string[0]
    
    for char in string:
        if char == result[-1]:
            continue
        
        result += char
    
    return result
# This code:

# 1. Checks if the string is empty and returns it if it is.
# (If `string` is empty, it makes the condition falsy, not executing the
# body, but the `not` operator flips it to `True`, so a truthy value,
# and executes the body returning the string.)

# 2. It assigns the character at index 0 of `string` to `result`.

# 3. The `for` loop iterates through the characters in `string` and if
# the current character is the same as the last character in `result`
# then nothing is done & it goes onto the next loop; 
#
# If it does not match, then the `if` statement doesn't execute and
# concatenates the current character to the string already assigned to
# `result`.

# 4. At the end of the function, the finalized string assigned to `result`
# is returned to the calling code.

# I like the use of the negative index (`[-1]`) to compare the current
# char to the last in the string-to-be-returned. It's easier to read &
# understand what's happening than the `index - 1` method I used.


