#imports the ability to get a random number (we will learn more about this later!)
from random import *


#Generates a random integer.
aRandomNumber = randint(1, 20)
# For Testing: print(aRandomNumber)
tries = 0
while tries is < 2
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric(): # checks if a string is only digits 0 to 9
	print("That's not a positive whole number, try again!")
    else:
	guess = int(guess) # converts a s.tring to an integer
    if guess == aRandomNumber:
        print("Congrats! You got it!")
        break
    elif guess > aRandomNumber
        print("Try again, that's too high.")
    else:
        print("Try again, that's too low.")
        tries = tries + 1
print("Sorry, the number was" + str(aRandomNumber)")
