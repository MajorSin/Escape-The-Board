#SETUP
import json

#GET DATA FROM JSON
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