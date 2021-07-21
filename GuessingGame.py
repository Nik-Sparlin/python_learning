# we will specify a secret word and have the user try to guess it until they get it
# create variable to store secret word
secret_word = "giraffe"

# store variable with user guesses
guess = ""

# create variable for number of guesses
guess_count = 0

# we also want to store a limit for user attempts
guess_limit = 3

# boolean that tells us if user has attempts left
out_of_guesses = False

# prompt user to guess secret word
# if they get it wrong, we need to prompt them to guess again until correct
# we also want to limit number of guesses
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

# we have two possible scenarios
if out_of_guesses:
    print("Out of tries; you lose.")
else:
    print("You guessed the secret word!")
