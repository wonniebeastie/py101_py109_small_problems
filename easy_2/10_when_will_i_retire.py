# PROBLEM
# Build a program that displays when the user will retire and how many 
# years she has to work till retirement.

# INPUTS
# An integer for age (user input)
# An integer for the age of retirement (user input)

# OUTPUTS
# The current year
# The year that the user will retire
# How long in years there is left til retirement

# MY SOLUTION
from datetime import date

current_age = int(input('What is your age? \n'))
age_of_retirement = int(input('At what age would you like to retire? \n'))

today = date.today()
current_year = today.year

def compute_retirement(age, retirement_age):
	print(f"It's {current_year}. "
	f"You will retire in {current_year + (retirement_age - age)}." 
	f"\nYou only have {retirement_age - age} years of work to go!")


compute_retirement(current_age, age_of_retirement)


# SOLUTION
from datetime import datetime

current_age = int(input('What is your current age? '))
retirement_age = int(input('At what age would you like to retire? '))

current_year = datetime.now().year
years_to_go = retirement_age - current_age
retirement_year = current_year + years_to_go

print(f"It's {current_year}. You will retire in {retirement_year}.")
print(f"You have only {years_to_go} years of work to go!")