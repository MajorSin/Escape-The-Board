#SETUP
import json


class post():
    def set(self):
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
    
    def display(self, vraag, antwoord, category, graad):
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
        #GA TERUG
        textFont(createFont("Segoe UI Bold", 32))
        fill("#978787")
        rect(20, 10, 200, 130, 28)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",52,85)
        #INGEVOEGD
        fill(250, 250, 250)
        text("Uw vraag was: " + vraag,60,185)
        text("Het antwoord is: " + antwoord,60,230)
        text("Bij de categorie: " + category,60,270)
        text("Met de moeilijkheidsgraad: " + graad,60,310)
        text("Uw vraag is toegevoegd!",60,360)
        
    def append(self, vraag, antwoord, category, graad):
        #APPEND
        entry = {"question": vraag, "answer": antwoord, "type": "open vraag", "category": category, "level": graad, "toevoeging": 'True'}
        filename = 'questions.json'
        with open(filename, "r") as file:
            data = json.load(file)
        data.append(entry)
        with open(filename, "w") as file:
            json.dump(data,file)
