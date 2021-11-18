import json

with open('questionsOriginal.json') as f:
    data = json.load(f)

file_dupli = open("questions.json", "w")
json.dump(data, file_dupli)
file_dupli.close()
