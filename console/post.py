#SETUP
import json

#INPUT
question = input("Welk vraag wilt u toevoegen?: ")
while question == "" or question == " ":
    print("\nU kunt dit niet leeg houden")
    question = input("Welk vraag wilt u toevoegen?: ")

answer = input("\nWat is het antwoord op dit vraag?: ")
while answer == "" or answer == " ":
    print("\nU kunt dit niet leeg houden")
    answer = input("Wat is het antwoord op dit vraag?: ")

category = input("\nIn welk categorie past dit (kennis of wiskunde)?: ").lower()
while category == "" or category == " " or (category != "kennis" and category != "wiskunde"):
    if category == "" or category == " ":
        print("\nU kunt dit niet leeg houden")
    else:
        print("\nKies uit kennis of wiskunde")
    category = input("In welk categorie past dit (kennis of wiskunde)?: ").lower()


#APPEND
filename = 'questions.json'
entry = {"question": question, "answer": answer,"category": category}
with open(filename, "r") as file:
    data = json.load(file)
data.append(entry)
with open(filename, "w") as file:
    json.dump(data,file)
print("\nToegevoegd!")