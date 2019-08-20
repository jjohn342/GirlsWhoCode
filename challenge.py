import random
iter = 0
# A list of words that
potential_words = ["roar", "lion", "book", "life"]

word = random.choice(potential_words)
print = (potential_words)
# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()
# Make it a list of letters for someone to guess

# TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 10
fails = 0

while guesses is not guess:
    guesses.append(guess)
    if guess == word:
        print(current_word)
        print("Congrats! You got it!")
        break

while fails < maxfails:
    guess = input("Guess a letter: ")
    if guess in word:
        print("Yes! Good job.")
        count += 1
    if guess not in word:
        print("Wrong! Try again!")
        count += 1
    for let in word:
        if let == word:
            current_word[iter] = word
        iter += 1
    for letter in range == (len(current_word)):
        for letter in range == 0(len(word)):
            print(current_word)
    if fails == 10:
        print(current_word)
        print("Sorry! You didn't guess it right.")

	# check if the guess is valid: Is it one letter? Have they already guessed it?
	# check if the guess is correct: Is it in the word? If so, reveal the letters!

print(current_word)

fails = fails+1
print("You have " + str(maxfails - fails) + " tries left!")
