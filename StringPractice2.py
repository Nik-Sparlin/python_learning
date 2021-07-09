# n\ creates a break in your string
# \" or \' allows you to use quotations within your string

print("Nik is allergic to bananas."
      "\nThis makes Nik sad."
      "\n\"Why am I allergic to bananas?\" they asked.")

# you can add to strings that you create
phrase = "Well shit."
print(phrase + " That\'s sad.")

# you can also use functions to make changes
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())

# and combine functions (in order of execution)
print(phrase.upper().isupper())

# you can use len() to determine the length of a string
print(len(phrase))

# and you can slice your data
# notice that the first letter "w" is at index 0
# this is because python uses zero-based indexing
print(phrase[0])
print(phrase[0:4])
print(phrase[5:])

# you can also combine strings and functions
# note that format allows you to replace {} with an integer from your index function
print(phrase.index("s"))
print("The letter \"s\" first appears in index {}.".format(phrase.index("shit")))

