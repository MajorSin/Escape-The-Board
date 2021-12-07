#SETUP
import json


class post():
    def set(self):
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
    
    def display(self, vraag, antwoord, category, graad):
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
        fill(0, 102, 153)
        rect(25,25,200,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #INGEVOEGD
        fill(250, 250, 250)
        text("Uw vraag was: " + vraag,400,175)
        text("Het antwoord is: " + antwoord,400,220)
        text("Bij de categorie: " + category,400,260)
        text("Met de moeilijkheidsgraad: " + graad,400,300)
        text("Uw vraag is toegevoegd!",400,340)
        
    def append(self, vraag, antwoord, category, graad):
        #APPEND
        entry = {"question": vraag, "answer": antwoord, "type": "open vraag", "category": category, "level": graad, "toevoeging": 'True'}
        filename = 'questions.json'
        with open(filename, "r") as file:
            data = json.load(file)
        data.append(entry)
        with open(filename, "w") as file:
            json.dump(data,file)
