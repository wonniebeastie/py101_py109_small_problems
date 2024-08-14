# PROBLEM
# Write a function that returns a list that contains every other 
# element of a list that is passed in as an argument. The values in the
# returned list should be those values that are in the 1st, 3rd, 5th, 
# and so on elements of the argument list.

# INPUTS
# A list

# OUTPUTS
# Returned list that have the values that are in the 1st, 3rd, 5th, and
# so on elements on the argument list.

# RULES (explicit + implicit)
# Try to solve the problem using list slicing.
# Input must be a list.
# Odd index values only in the returned list.

# MY SOLUTION
def oddities(list):
	odd_list = list[::2]
	return odd_list
# Oh oops, did not realize the slicing syntax was only supposed to be
# used for the bonus question.

oddities(["a", "b", "c", "d", "e"])
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True


# SOLUTION
def oddities(lst):
    result = []
    for idx in range(len(lst)):
        if idx % 2 == 0:
            result.append(lst[idx])

    return result

# This problem can be slightly confusing since we want the 1st, 3rd, 
# 5th, and so on elements of the list, but these correspond to elements
# with indexes 0, 2, 4, etc. As long as you keep that in mind, there are
# many different ways to solve this problem correctly.

# In this approach:

# - We loop through all indexes of the list using range(len(lst)).

# - In the loop, we check if the current index idx is even using the 
# condition idx % 2 == 0. If it is even, it means we have an 
# odd-numbered element (1st, 3rd, 5th, etc.), so we append the element 
# to the result list. 

# - After iterating through all indexes, we return the result list.


# BONUS SOLUTION
# The bonus solution takes advantage of Python's list slicing, which 
# lets us start from the first element and skip every second element to
# get the desired result. Python makes it relatively easy to extract 
# every other element using the slicing mechanism, which proves to be 
# both concise and efficient. The [::2] syntax retrieves elements from 
# the list starting from the beginning to the end, skipping every other
# element.