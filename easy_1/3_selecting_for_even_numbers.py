# Print all even numbers from 1 to 99, inclusive, with each number on 
# a separate line.

# Bonus Question: Can you solve the problem by iterating over just the 
# even numbers?


# INPUTS
# Numbers 1 to 99, inclusive

# OUTPUTS
# Even numbers from 1 to 99, inclusive

# RULES (explicit + implicit)
# Print only the even numbers 
# Numbers must be on separate lines.

# OBJECTS TO BE USED
# Range function
# `for` loop

# PSEUDOCODE
# For each number in range of 1 to 99, inclusive,
#     If the number is even,
#       Print number


# MY SOLUTION
for num in range(1, 100):
    if num % 2 == 0:
        print(num)

# BONUS Q
for number in range(0, 100, 2):
    if number > 0:
        print(number)


# SOLUTION
# Same as mine.

# BONUS S
for number in range(2, 100, 2):
    print(number)
# LMAO I didn't think to start from 2.
# Hilarious