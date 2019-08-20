import json

#create an empty dictionary
#create a list of survey questions
print("Welcome to my survey!")

questions = [
    "Did you use your phone today?",
    "How old are you?",
    "Do you like coding?",
    "Would you want a pet python or a sloth? Or neither?",
    "What food do you like?",
    ]

#create a list of related keys
key = ["phone", "year", "coding", "animals", "food"]

#loop through your list of survey questions and take user input for responses
all_users = []
done = "no"

while done == "no":
    users = {}
    i = 0
    for w in questions:
        answers = input(w + " ")
        users[key[i]] = answers
        i += 1
    all_users.append(users)
    done = input("Have you gathered your information? (yes or no):")

print(all_users)
with open("survey.json") as f:
    try:
        olddata = json.load(f)
    except ValueError:
        olddata = []
all_users.extend(olddata)
f.close()

#print your dictionary
#print(all_users)

f = open("survey.json", "w")
json.dump(all_users, f)
f.close()

count = 0
phonecount = 0

for u in all_users:
    count += 1
    answer = u["phone"]
    if answer == "yes":
        phonecount += 1
print(str(phonecount) + "out of" + str(count) + "used their phones today!")
