#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")
print(type(f))
print("Can your password survive a dictionary attack?")

password = []
#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
newpassword = test_password.strip()

#Write logic to see if the password is in the dictionary file below here:


for line in f:
    newitem = line.strip()
    if newitem == newpassword:
        print("Denied! Too weak!")
