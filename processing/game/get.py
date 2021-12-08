#SETUP
import json

#GET DATA FROM JSON

class get():
    def set(self):
        #SET BG
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
        
    def display(self):
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
        fill(0, 102, 153)
        #GA TERUG
        textFont(createFont("Segoe UI Bold", 32))
        fill("#978787")
        rect(20, 10, 200, 130, 28)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",52,85)
        #JSON DATA
        json_file = open('questions.json')
        list = json.loads(json_file.read())
        #PRINT RESULT
        height = 180
        questions = 1
        heightQuestion = 250
        fill(250, 250, 250)
        for i in range(len(list)):
            main = list[i]
            if main['toevoeging'] == 'True' and main['type'] == "open vraag":
                textFont(createFont("Segoe UI Bold", 19))
                textSize(45)
                text(questions, 20, heightQuestion)
                textSize(19)
                text("Vraag is: " + main['question'], 80, height)
                height += 45
                text("Antwoord is: " + main['answer'], 80, height)
                height += 45
                text("Uit de categorie: " + main['category'], 80, height)
                height += 45
                text("Met de moeilijkheidsgraad: " + main['level'], 80, height)
                height += 45
                text("-----------------------", 80, height)
                height += 50
                heightQuestion += 240
                questions += 1
