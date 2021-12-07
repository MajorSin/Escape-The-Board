#SETUP
import json

#GET DATA FROM JSON

class get():
    def set(self):
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
        
    def display(self):
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
        fill(0, 102, 153)
        #GA TERUG
        rect(25,25,200,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #JSON DATA
        json_file = open('questions.json')
        list = json.loads(json_file.read())
        #PRINT RESULT
        textSize(20)
        height = 150
        questions = 1
        fill(250, 250, 250)
        for i in range(len(list)):
            main = list[i]
            if main['toevoeging'] == 'True' and main['type'] == "open vraag":
                text("VRAAG " + str(questions) + '\n', 80, height)
                height += 50
                text("Vraag is: " + main['question'], 80, height)
                height += 50
                text("Antwoord is: " + main['answer'], 80, height)
                height += 50
                text("Uit de categorie: " + main['category'], 80, height)
                height += 50
                text("-----------------------", 80, height)
                height += 50
                questions += 1
