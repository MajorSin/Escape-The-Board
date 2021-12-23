#SETUP
import json

class post():
    def prep(self):
        global bgImg
        bgImg = loadImage("images/main-background.jpg")
    
    def display(self, vraag, antwoord, category, graad):
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
        text("Uw vraag was: " + vraag,25,185)
        text("Het antwoord is: " + antwoord,25,230)
        text("Bij de categorie: " + category,25,270)
        text("Met de moeilijkheidsgraad: " + graad,25,310)
        text("Uw vraag is toegevoegd!",25,360)
        
    def append(self, vraag, antwoord, category, graad):
        #APPEND
        entry = {"question": vraag, "answer": antwoord, "type": "open vraag", "category": category, "level": graad, "toevoeging": 'True'}
        filename = 'data/questions.json'
        with open(filename, "r") as file:
            data = json.load(file)
        data.append(entry)
        with open(filename, "w") as file:
            json.dump(data,file)
