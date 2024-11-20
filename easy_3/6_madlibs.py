# Create a simple madlib program that prompts for a noun, a verb, an 
# adverb, and an adjective, and injects them into a story that you 
# create.

# Ex:
# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly

# Ex Output:
# Do you walk your blue dog quickly? That's hilarious!
# The blue dog walks quickly over the lazy dog.
# The dog quickly walks up to Joe's blue turtle.

noun = input('Enter a noun: ')
verb = input('Enter a verb: ')
adjective = input('Enter an adjective: ')
adverb = input('Enter an adverb: ')

print(f"I saw a really big {noun} the other day.")
print(f"It was the first time I saw such a {adjective} {noun}!")
print(f"I {verb}ed over to it as {adverb} as I can.")
print(f"I can't wait to do it again!")

