# PROBLEM
# Write a program that asks for user's name, then greets the user. 
# If the user appends a `!` to their name, the computer will yell the 
# greeting (print it using all uppercase).

# EXAMPLE 1
# What is your name? Sue
# Hello Sue.

# EXAMPLE 2
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

# INPUTS
# User input of a name
# User input of a name with a `!`

# OUTPUTS
# Greeting with the name
# OR
# Greeting with everything capitalized to imitate yelling if the user
# adds a `!` to their name. 

# RULES (explicit + implicit)
# Ask for user's name
# Greet user using the name.
# Greet user with all capital letters if they append a `!` to their name


# MY SOLUTION
def say_greeting(name):
	# print(name)
	if '!' in name:
		print(f'HELLO {name.upper()} I SEE YOU ENJOY BEING YELLED AT!')
	else:
		print(f'Hello {name}.')

user_name = input("What is your name? (Type '!' if you want to be yelled at): \n")

# print(user_name)

say_greeting(user_name)


# SOLUTION
name = input("What is your name? ")

if name.endswith("!"):
    print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
else:
    print(f"Hello {name}.")

# We use the `input` function to obtain the user's input.
# We then use `str.endswith` method to determine if the name ends with
# a `!`.