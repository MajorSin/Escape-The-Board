#SETUP
import json


class post():
    def set(self):
        background(0, 200, 0)
        True
    
    def display(self, vraag, antwoord, category):
        background(0, 200, 0)
        fill(0, 102, 153)
        rect(25,25,200,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #INGEVOEGD
        text("Uw vraag was: " + vraag,400,175)
        text("Het antwoord is: " + antwoord,400,220)
        text("Bij de categorie: " + category,400,260)
        text("Uw vraag is toegevoegd!",400,300)
        
    def append(self, vraag, antwoord, category):
        #APPEND
        entry = {"question": vraag, "answer": antwoord,"category": category, "toevoeging": 'True'}
        filename = 'questions.json'
        with open(filename, "r") as file:
            data = json.load(file)
        data.append(entry)
        with open(filename, "w") as file:
            json.dump(data,file)
