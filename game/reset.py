import json

class reset():
    global toevoeging
    def set(self):
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
    
    def display(self):
        global toevoeging
        bgImg = loadImage("img/achtergrond.jpg")
        background(bgImg)
        #GA TERUG
        textFont(createFont("Segoe UI Bold", 32))
        fill("#978787")
        rect(20, 10, 200, 130, 28)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",52,85)
        #LEEG
        json_file = open('json/questions.json')
        list = json.loads(json_file.read())
        toevoeging = False
        for i in range(len(list)):
            main = list[i]
            if main['toevoeging'] == 'True':
                toevoeging = True
        if toevoeging != True:
            fill(250, 250, 250)
            text("Er zijn geen toegevoegde vragen",400,165)
        #NIET LEEG
        else:
            #BEVESTIGING
            fill("#640700")
            rect(415,205,450,100)
            fill(250, 250, 250)
            text("Weet u het zeker?",515,165)
            text("Ja",630,262)
    
    def reset2(self):
        if toevoeging == True:
            self.delete()
            bgImg = loadImage("img/achtergrond.jpg")
            background(bgImg)
            #GA TERUG
            textFont(createFont("Segoe UI Bold", 32))
            fill("#978787")
            rect(20, 10, 200, 130, 28)
            textSize(32)
            fill(100, 0, 53)
            text("Ga Terug",52,85)
            #KNOP BEVESTIGING
            textSize(30)
            fill(250, 250, 250)
            text("Vragen gereset naar originele staat!",375,180)
        
    def delete(self):
        if toevoeging == True:
            with open('json/questionsOriginal.json') as f:
                data = json.load(f)
    
            file_dupli = open("json/questions.json", "w")
            json.dump(data, file_dupli)
            file_dupli.close()
