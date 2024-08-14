# PROBLEM
# Write a program that prompts the user for two positive numbers 
# (floating-point), then prints the results of the following operations
# on those two numbers: addition, subtraction, product, quotient, floor 
# quotient, remainder, and power. Do not worry about validating the 
# input.

# EXAMPLES
# ==> Enter the first number:
# 3.141529
# ==> Enter the second number:
# 2.718282
# ==> 3.141529 + 2.718282 = 5.859811
# ==> 3.141529 - 2.718282 = 0.42324699999999993
# ==> 3.141529 * 2.718282 = 8.539561733178
# ==> 3.141529 / 2.718282 = 1.1557038600115808
# ==> 3.141529 // 2.718282 = 1.0
# ==> 3.141529 % 2.718282 = 0.42324699999999993
# ==> 3.141529 ** 2.718282 = 22.45792517468373

# INPUTS
# 2 positive floating-point numbers (user input)

# OUTPUTS
# Printed results of operations on the two numbers: addition, 
# subtraction, product, quotient, floor quotient, remainder, 
# and power.

# RULES (explicit + implicit)
# The numbers are floats.
# Don't worry about input validation.

def prompt(message):
	return f'--> {message}'

num1 = float(input(prompt("Enter the first number: ")))
num2 = float(input(prompt("Enter the second number: ")))

print(prompt(f'{num1} + {num2} = {num1 + num2}'))
print(prompt(f'{num1} - {num2} = {num1 - num2}'))
print(prompt(f'{num1} * {num2} = {num1 * num2}'))
print(prompt(f'{num1} / {num2} = {num1 / num2}'))
print(prompt(f'{num1} // {num2} = {num1 // num2}'))
print(prompt(f'{num1} % {num2} = {num1 % num2}'))
print(prompt(f'{num1} ** {num2} = {num1 ** num2}'))


# SOLUTION 1

first_float = float(input("==> Enter the first number:\n"))
second_float = float(input("==> Enter the second number:\n"))

print(f"{first_float} + {second_float} = "
    f"{first_float + second_float}")
print(f"{first_float} - {second_float} = "
    f"{first_float - second_float}")
print(f"{first_float} * {second_float} = "
      f"{first_float * second_float}")
print(f"{first_float} / {second_float} = "
    f"{first_float / second_float}")
print(f"{first_float} // {second_float} = "
      f"{first_float // second_float}")
print(f"{first_float} % {second_float} = "
    f"{first_float % second_float}")
print(f"{first_float} ** {second_float} = "
      f"{first_float ** second_float}")

# This solution is straightforward, but repetitive and error-prone,
# especially if you want to add a number of other mathematical 
# operations.



# SOLUTION 2
def calculate(first, second, operator):
    match operator:
        case '+':  return first + second
        case '-':  return first - second
        case '*':  return first * second
        case '/':  return first / second
        case '//': return first // second
        case '%':  return first % second
        case '**': return first ** second

first_float = float(input("==> Enter the first number:\n"))
second_float = float(input("==> Enter the second number:\n"))
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f"{first_float} {operator} {second_float}"
    result = calculate(first_float, second_float, operator)
    print(f"==> {operation} = {result}")

# This solution addresses the bulk of the reptitiveness by 
# using a helper function (`calculate`) to calculate & using a loop to 
# perform the operations & print the results. It needs a bit more 
# code and a bit more effort to understand, but this code will be easier
# maintain in the long term.

# Both solutions ignore what happens when an input value isn't a valid
# number, or if the second number is a zero-value. In both cases, the 
# code will raise an exception. 


