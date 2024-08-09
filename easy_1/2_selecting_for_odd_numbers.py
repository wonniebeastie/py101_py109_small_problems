# PROBLEM
# Print all odd numbers from `1` to `99`, inclusive, with each number
# on a separate line.

# Bonus Question: 
# Can you solve the problem by iterating over just the odd numbers?

# INPUTS
# Integers `1` to `99`, inclusive

# OUTPUTS
# All odd numbers in `1` to `99`, inclusive 

# RULES (explicit + implicit)
# `1` & `9` should be inclusive
# Each number should be on a separate line in the output.


# OBJECTS TO BE USED
# Range
# List comprehension

# PSEUDOCODE
# one_to_ninetynine = range of 1 to 99, inclusive
# [ Print number for each number in iterable if odd number ]


# MY SOLUTION
for _ in range(1, 100):
    if _ % 2 != 0:
        print(_)


# BONUS Q
one_to_ninetynine = range(1, 100)

[ print(num) for num in range(1, 100) if num % 2 != 0 ]


# SOLUTION 
for number in range(1, 100):
    if number % 2 == 1:
        print(number)
# We use Python's `range` function to iterate over all numbers from `1`
# to `99`.
# Then it check whether each number is odd using the condition 
# `number % 2 == 1`.
# Then prints it.

# BONUS S
for number in range(1, 100, 2):
    print(number)
# We use the `step` value of the `range` function to increment by `2`,
# starting from `1`.
# This ensures that we only iterate over odd numbers.


# FURTHER EXPLORATION

starting_num = int(input('Enter the starting number, inclusive: '))
ending_num = int(input('Enter the ending number, exclusive: '))

def select_odd(start, end):
    for num in range(start, end):
        if num % 2 != 0:
            print(num)

select_odd(starting_num, ending_num)