# PROBLEM
# The or operator returns a truthy value if either or both of its 
# operands are truthy, a falsy value if both operands are falsy. 
# The and operator returns a truthy value if both of its operands are
# truthy, and a falsy value if either operand is falsy. This works great
# until you need only one of two conditions to be truthy, the so-called 
# exclusive or, also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function that takes two 
# arguments, and returns True if exactly one of its arguments is 
# truthy, False otherwise.


# INPUTS
# 2 values

# OUTPUTS
# True or False

# RULES (explicit + implicit)
# Just one, not more or less, needs to be truthy in order for the 
# function to return True.

# OBJECTS TO BE USED
# 

# PSEUDOCODE
# SET `xor(value1, value2)`
#      IF value1 == truthy and value2 == falsy, return True
#      ELSE IF value1 == falsy and value2 == truthy, return True
#      ELSE return False


# MY SOLUTION
def xor(value1, value2):
	if (bool(value1) == True) and (bool(value2) == False):
		return True
	elif (bool(value1) == False) and (bool(value2) == True):
		return True
	else:
		return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)


# SOLUTION
def xor(value1, value2):
    if (value1 and not value2) or (value2 and not value1):
        return True

    return False