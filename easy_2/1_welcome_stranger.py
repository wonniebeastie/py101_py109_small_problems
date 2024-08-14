# PROBLEM
# Create a function that takes 2 arguments: a list and a dictionary. 
# The list will contain 2 or more elements that, when joined with spaces, 
# will produce a person's name. The dictionary will contain two keys, 
# "title" and "occupation", with the appropriate values. 
# Your function should return a greeting that uses the person's full name 
# and mentions the person's title.

# EXAMPLE:
# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

# INPUTS
# 2 Arguments - a list & a dictionary

# OUTPUTS
# A greeting that uses the person's full name & title.

# RULES (explicit + implicit)
# List - 2 or more elements that will form a person's name when joined
# with spaces.
# Dictionary - 2 keys, "title" & "occupation", and their values.

# OBJECTS TO BE USED
# List
# Dictionary
# Function

# PSEUDOCODE
# SET `name` = "Max", "Imus", "Ki-Diaz"
# SET `title_occu` = 
#     "title": "The Lounger", 
#     "occupation": "Being Cute"

# SET FUNCTION `greeting(name_list, occu_dict)`
#     PRINT "
#     Hello, {name (values separated into string literals)}! 
#     What a great opportunity to see the great 
#     {occu_dict (values separated into string literals)}!"

max = ["Max", "Imus", "Ki-Diaz"]
max_occu = {"title": "Lounger", "occupation": "Lounging"}

def greeting(name, title_occu):
	# print(name)
	# print(title_occu)
	name = ' '.join(name)
	# print(name)
	title_occu = ' '.join(title_occu.values())
	# print(title_occu)
	return f'Hello, {name}! What a pleasure to see the great {title_occu}!'
# I used `print()` the first time around, but the question says to return it.

greeting(max, max_occu) 
# Hello, Max Imus Ki-Diaz! What a pleasure to see the great Lounger Lounging!


# SOLUTION
def greetings(name, status):
    return(f"Hello, {' '.join(name)}! Nice to have a "
		f"{status['title']} {status['occupation']} "
		"around.")

print(greetings(max, max_occu)) 
# Hello, Max Imus Ki-Diaz! Nice to have a Lounger Lounging around.

# The `join` method is used to change the list into a full name with 
# appropriate spacing. For the dictionary, we access the items by their
# keys. 

# Finally, we use f-string formatting to combine everything into a
# single string, resulting in a concise and readable way to format the
# final output.
