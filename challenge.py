import random
iter = 0
# A list of words that
potential_words = ["christmas", "lion", "books", "life"]

word = random.choice(potential_words)
print = (potential_words)
# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()
letters = ["a, q, z, w, s, x, c, d, e, v, f, r, t, g, b, h, y, n, m, j, u, i, k, l, o, p"]
# Make it a list of letters for someone to guess

current_word = ["_","_","_","_","_","_","_","_","_"]
life_word = ["_","_","_","_"]
 # TIP: the number of letters should match the word
books_word = ["_","_","_","_","_"]

lion_word = ["_","_","_","_"]

for let in word:
    if let == word:
        current_word[iter] = word
    iter += 1


# Some useful variables
guesses = [5]
maxfails = 10
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
if guess in word:
    print("Yes! Good job.")
    count += 1
if guess not in word:
    print("Wrong! Try again!")
    count += -1
	# check if the guess is valid: Is it one letter? Have they already guessed it?
	# check if the guess is correct: Is it in the word? If so, reveal the letters!

print(current_word)

fails = fails+1
print("You have " + str(maxfails - fails) + " tries left!")
