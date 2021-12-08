import json
import random

used_makkelijk = []

class vraag():
    #STANDAARD SCHERM
    def display(self,makkelijkButton, category):
        bgImg = loadImage("img/Vachtergrond.jpg")
        background(bgImg)
        noStroke()
        #ANNULEER
        fill(250, 250, 250)
        textFont(createFont("Segoe UI Bold", 25))
        textSize(32)
        text("Annuleer",55,75)
        #CATEGORIE
        text("Categorie: " + category,900,75)
        #LAAT VRAAG ZIEN
        self.vraagStart(category)
        
    #LAAT VRAAG ZIEN
    def vraagStart(self, category):
        global main
        global index
        textFont(createFont("data/Bungee-Regular.ttf", 25))
        fill(250,250,250)
        index_random = []
        json_file = open('questions.json')
        data = json.loads(json_file.read())
        for i in range(len(data)):
            main = data[i]
            if category == "standaard":
                if main['level'] == "makkelijk":
                    if i not in used_makkelijk:
                        index_random.append(i)
            elif main['level'] == "makkelijk" and main['category'] == category:
                if i not in used_makkelijk:
                    index_random.append(i)
        try:
            index = random.choice(index_random)
            main = data[index]
            text(main['question'],15,150)
            #MTP
            if main['type'] == "mtp":
                text("A: " + str(main['A']),15,225)
                text("B: " + str(main['B']),395,225)
                text("C: " + str(main['C']),770,225)
            #ANTWOORD 
            fill("#f56600")
            rect(10,290,475,100)
            fill(100, 0, 53)
            text("Laat antwoord zien", 90, 345)
        except:
            text("Er zijn geen vragen meer!",400,150)
            
    #LAAT ANTWOORD ZIEN
    def antwoord(self):
        fill(250,250,250)
        used_makkelijk.append(index)
        text(main['answer'], 495, 345)
        
    #MOUSEPRESSED
    def mousePressed(self, vraagButton):
        #ANTWOORD LATEN ZIEN
        if 10 < mouseX < 10 + 475 and 290 < mouseY < 290 + 100 and vraagButton == True:
            self.antwoord()
