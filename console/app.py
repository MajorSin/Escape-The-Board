#IMPORT
import json
import random

#KEUZE MAKEN
graad = ""
while graad != "a" and graad != "b" and graad != "c":
    graad = input("Kies een optie:\nA: Moeilijk\nB: Makkelijk\nC: Einde\n").lower()

#VRAAG
used_makkelijk = []
used_moeilijk = []
while graad == "a" or graad == "b":
    json_file = open('questions.json', encoding="UTF8")
    data = json.loads(json_file.read())
    #MOEILIJK
    if graad == "a":
        index_random = []
        for i in range(len(data)):
            main = data[i]
            if main['level'] == "moeilijk":
                if i not in used_moeilijk:
                    index_random.append(i)
        #try:
        index = random.choice(index_random)
        main = data[index]
        print("Vraag is:", main['question'])
        if main["type"] == "mtp":
            print("A:", main["A"], "\nB:", main["B"], "\nC:", main["C"])
        #ANTWOORD VRAGEN
        antwoord = input("Wilt u antwoord zien (Ja/Nee)? ").lower()
        if antwoord == "ja":
            print("Het antwoord is:", main['answer'])
            used_moeilijk.append(index)
        print("\n")
        #except:
        #    print("Er zijn geen vragen meer!\n")
    #MAKKELIJK
    elif graad == "b":
        index_random = []
        for i in range(len(data)):
            main = data[i]
            if main['level'] == "makkelijk":
                if i not in used_makkelijk:
                    index_random.append(i)
        try:
            index = random.choice(index_random)
            main = data[index]
            print("Vraag is:", main['question'])
            if main["type"] == "mtp":
                print("A:", main["A"], "\nB:", main["B"], "n\C:", main["C"])
            #ANTWOORD VRAGEN
            antwoord = input("Wilt u antwoord zien (Ja/Nee)? ").lower()
            if antwoord == "ja":
                print("Het antwoord is:", main['answer'])
                used_makkelijk.append(index)
            print("\n")
        except:
            print("Er zijn geen vragen meer!\n")
    #INPUT
    graad = input("Kies een optie:\nA: Moeilijk\nB: Makkelijk\nC: Einde\n").lower()

#EINDE
print("\nEinde programma")