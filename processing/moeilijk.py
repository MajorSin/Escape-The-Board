import json
import random

used_moeilijk = []

class moeilijk():
    #STANDAARD SCHERM
    def display(self,moeilijkButton):
        background(0, 200, 0)
        #GA TERUG
        background(0, 200, 0)
        fill(0, 102, 153)
        rect(25,25,200,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #LAAT VRAAG ZIEN
        self.moeilijkStart()
        
    #LAAT VRAAG ZIEN
    def moeilijkStart(self):
        global main
        global index
        index_random = []
        json_file = open('questions.json')
        data = json.loads(json_file.read())
        for i in range(len(data)):
            main = data[i]
            if main['level'] == "moeilijk":
                if i not in used_moeilijk:
                    index_random.append(i)
        try:
            index = random.choice(index_random)
            main = data[index]
            text(main['question'],380,150)
            #ANTWOORD 
            fill(0, 102, 153)
            rect(300,210,475,100)
            fill(100, 0, 53)
            text("Laat antwoord zien", 385, 265)
        except:
            text("Er zijn geen vragen meer!",400,150)
            
    #LAAT ANTWOORD ZIEN
    def antwoord(self):
        used_moeilijk.append(index)
        fill(100, 0, 53)
        text(main['answer'], 395, 350)
