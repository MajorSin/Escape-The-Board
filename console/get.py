#SETUP
import json

#CATEGORY
category_Get = input("Uit welk categorie?\nA. Kennis\nB. Wiskunde\nC. Allebei\n").lower()
while category_Get != "a" and category_Get != "b" and category_Get != "c":
    print("\nU moet a, b of c kiezen.")
    category_Get = input("Kies een letter: ").lower()
print(category_Get)

#GET DATA FROM JSON
json_file = open('questions.json')
list = json.loads(json_file.read())
questions = 1

#PRINT RESULT
print("\n")
#A. Kennis
if category_Get == "a":
    for i in range(len(list)):
        main = list[i]
        if main['category'] == "kennis":
            print("VRAAG " + str(questions) + '\n')
            print("Vraag is:", main['question'])
            print("Antwoord is:", main['answer'])
            print("Uit de categorie:", main['category'])
            print("-----------------------")
            questions += 1
#B. Wiskunde
elif category_Get == "b":
    for i in range(len(list)):
        main = list[i]
        if main['category'] == "wiskunde":
            print("VRAAG " + str(questions) + '\n')
            print("Vraag is:", main['question'])
            print("Antwoord is:", main['answer'])
            print("Uit de categorie:", main['category'])
            print("-----------------------")
            questions += 1
#C. ALLE VRAGEN VRAGEN
elif category_Get == "c":
    for i in range(len(list)):
        main = list[i]
        print("VRAAG " + str(i+1) + '\n')
        print("Vraag is:", main['question'])
        print("Antwoord is:", main['answer'])
        print("Uit de categorie:", main['category'])
        print("-----------------------")
        questions += 1