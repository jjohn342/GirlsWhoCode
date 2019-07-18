# --- Define your functions below! ---
def intro():
    print("Hi! My name is Jolina! Welcome!")
    print("Type something!")

def process_input(answer):
    if is_valid_input(answer):
        say_greetings()
    else:
        say_default()
    if answer == "Good":
        say_question()
    if in_valid_input(answer):
        say_joke()
    else:
        say_pun(answer)


def is_valid_input(answer):
    valid = ["hi, Hi, hello, Hello, hey, Hey,"]
    if answer in valid:
        return True
    else:
        return False

def in_valid_input(answer):
    valid_list = ["It has a virus, virus, Virus, it has a virus, it had a virus, It had a virus"]
    if answer in valid_list:
        return True
    else:
        return False

def say_greetings():
    print("Hello! Glad to see you here!")
    print("How are you?")

def say_default():
    print("I hope your day is good!")

def say_question(answer):
    print("That's refreshing to hear!")


def say_pun(answer):
        print("Are you Santa? Because you arrived to my chat in the Nick of time!")
        print("Haha! Get it? Nick of time?! lol")

def say_joke(answer):
    print("Why did the computer sneeze?")
    if answer == "It has a virus":
        print("Congrats! You got it!")


def say_otherjoke(answer):
    print("What did the computer do at lunch time?")
    if answer == "Had a byte":
        print("Congrats! You got it!")


# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?)")
        process_input(answer)
        answer = input("Do you want to listen to my joke?")
        say_joke(answer)
        answer = input("What do you think the answer is?")
        if answer == ("It had a virus"):
            print("Congrats! You picked the right answer!")
        else:
            print("Sorry! The answer was that it had a virus.")
        answer = input("Do you want to listen to my other joke?")
        say_otherjoke(answer)
        answer = input("What do you think the answer is?")
        if answer == "It had a byte":
            print("Congrats! You got it!")
            print("Anyways, thanks for stopping by in my chat! I hope you had a punny time!")
        else:
            print("Sorry that's not right! The answer was that it had a byte.")
            print("Wait wait! One more! A bicycle can't stand on its own because it is two-tired.")
            print("Anyways, thanks for stopping by in my chat!I hope you had a punny time!")
            break


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
