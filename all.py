#SETUP
import json

#KEUZE MAKEN
print("Kies uit de volgende taken: \nA: Alle vragen + antwoorden inzien\nB: Vraag toevoegen\nC: Vraag verwijderen")
choice = input("\nKies een letter: ").lower()
while choice != "a" and choice != "b" and choice != "c":
    print("\nU moet a, b of c kiezen.")
    choice = input("Kies een letter: ").lower()

#VRAGEN MET ANTWOORDEN INZIEN
if choice == 'a':
    print("\n\n-----------------------")

    json_file = open('questions.json')
    list = json.loads(json_file.read())

    #PRINT RESULT
    for i in range(len(list)):
        main = list[i]
        print("VRAAG " + str(i+1) + '\n')
        print("Vraag is:", main['question'])
        print("Antwoord is:", main['answer'])
        print("Uit de categorie:", main['category'])
        print("-----------------------")
#VRAAG TOEVOEGEN
elif choice == 'b':
    #INPUT
    print("\n\n")
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
#VRAAG VERWIJDEREN
elif choice == 'c':
    print("Nog niet beschikbaar.")
#ERROR
else:
    print("Oeps, iets ging mis. Probeer het opnieuw")
