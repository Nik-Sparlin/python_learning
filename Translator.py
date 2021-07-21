# we can take in a string and translate it into another language
# giraffe language: any vowel becomes a g
# dog = dgg cat = cgt

# make a translate function
def translate(phrase):
    # create variable to store translation
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
