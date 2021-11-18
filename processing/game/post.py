#SETUP
import json

#APPEND
entry = {"question": vraag, "answer": antwoord,"category": category}
filename = 'questions.json'
with open(filename, "r") as file:
    data = json.load(file)
data.append(entry)
with open(filename, "w") as file:
    json.dump(data,file)
print("\nToegevoegd!")
