# PROBLEM
# Create a simple tip calculator. 
# The program should prompt for a bill amount and a tip rate. 
# The program must compute the tip, then print both the tip and the 
# total amount of the bill. 
# You can ignore input validation and assume that the user will enter 
# valid numbers.

# EXAMPLE
# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

# INPUTS
# User input: bill amount
# User input: tip rate

# OUTPUTS
# Tip amount
# Total bill amount

# RULES (explicit + implicit)
# Must get the bill & tip rate from the user.
# Program must compute the tip.
# Then print both the tip & the total amount of the bill.
# Input validation can be ignored.

# PSEUDOCODE
# SET `prompt(message)`:
#     Append `--->` to the beginning of `message`
#
# PRINT `prompt('Welcome to the Tip Calculator!')` 
# 
# 
# SET `calculate_total_bill(bill, tip_r)`:
#   SET `initial_bill` = GET input from user '---> What is the bill?: '
#   SET `tip_percentage` = GET input from user '---> What is the tip percentage?: '
#
#   SET `tip_amount` = `tip_precentage` converted to float * `initial_bill` converted to float
#   SET `final_bill` = `tip_amount` + `initial_bill` converted to float
#
#   PRINT `prompt('The tip is {`tip_amount`}.')`
#   PRINT `prompt('The total is {`final_bill`}.')`


# MY SOLUTION
def prompt(message):
    message = '---> ' + message
    return message

print(prompt('Welcome to the Tip Calculator!'))

initial_bill = float(input(prompt('What is the bill?: \n')))
tip_percentage = float(input(prompt('What is the tip percentage? \n'))) / 100

def calculate_total_bill(initial_amount, tip_rate):
    tip_amount = tip_rate * initial_amount
    final_bill = tip_amount + initial_amount
    
    print(prompt(f'The tip amount is: \n{tip_amount:.2f}'))
    print(prompt(f'Your total bill is: \n{final_bill:.2f}'))

calculate_total_bill(initial_bill, tip_percentage)


# SOLUTION
bill = float(input("What is the bill? "))
percentage = float(input("What is the tip percentage? "))

tip = bill * (percentage / 100)
total = bill + tip

print(f"The tip is ${tip:.2f}")
print(f"The total is ${total:.2f}")
# This solution collects user input, converts it to a floating-point 
# number, then calculates the `tip` & `total` amount.
# The result is formatted to two decimal places using f-strings.
#
# Consider a scenario in which we didn't explicitly convert the inputs 
# using float. 
# If we attempted to compute `tip` without the conversion, Python 
# would raise a `TypeError`, indicating that unsupported operand types
# were being used for the multiplication.
#
# Since in Python, there's a clear distinction between string and
# number operations, always be sure to convert input strings to the 
# appropriate numeric type before doing calculations.