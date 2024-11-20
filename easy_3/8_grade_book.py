# Write a function that determines the mean (average) of the three 
# scores passed to it, and returns the letter associated with that 
# grade.

# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'
# Tested values are all between 0 and 100. There is no need to check 
# for negative values or values greater than 100.



# INPUTS & OUTPUTS
# I: integer, integer, integer
# O: 1 char string

# EXAMPLE(S)
# I: 95, 90, 93
# O: A

# I: 50, 50, 95
# O: D

# RULES (EXPLICIT/IMPLICIT)
# - Don't need to do input validation.
# - Tested values are between `0` & `100`
# - Must find average of 3 parameters - add the 3 parameters together,
#   divide them by 3.
# - The returned value must have a string associated with it from a range

# QUESTIONS / BRAINSTORM
# - Use a match statement to return string associated with int value

# GOAL
# To take 3 scores & find the average and return the letter grade 
# associated with that average.

# STEPS
# Define function `get_grade` (3 int parameters)
#     SET `average` = (int + int + int) // 2
#  

def get_grade(score1, score2, score3):
	average = (score1 + score2 + score3) // 3

	if 90 <= average <= 100:
		return "A"
	elif 80 <= average < 90:
		return "B"
	elif 70 <= average < 80:
		return "C"
	elif 60 <= average < 70:
		return "D"
	else:
		return "F"

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True

# The solution first computes the average of the three scores. It then
# determines the letter grade equivalent via a series of if statements 
# in accordance with the problem specification.

# Note that this code takes advantage of Python's ability to use 
# multiple comparison operators in the same expression. In this code, 
# 80 <= average < 90 is equivalent to the more wordy (80 <= average) and (average < 90).