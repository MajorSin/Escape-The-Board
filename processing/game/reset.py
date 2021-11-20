import json

class reset():
    global toevoeging
    def set(self):
        background(0, 200, 0)
    
    def display(self, buttonPressedResetten2):
        global toevoeging
        background(0, 200, 0)
        fill(0, 102, 153)
        rect(25,25,200,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #LEEG
        json_file = open('questions.json')
        list = json.loads(json_file.read())
        toevoeging = False
        for i in range(len(list)):
            main = list[i]
            if main['toevoeging'] == 'True':
                toevoeging = True
        if toevoeging != True:
            text("Er zijn geen toegevoegde vragen",400,165)
        #NIET LEEG
        else:
            #BEVESTIGING
            fill(0, 102, 153)
            rect(300,205,450,100)
            fill(100, 0, 53)
            text("Weet u het zeker?",400,165)
            text("Ja",505,260)
    
    def reset2(self):
        if toevoeging == True:
            self.delete()
            background(0, 200, 0)
            fill(0, 102, 153)
            rect(25,25,200,80)
            textSize(32)
            fill(100, 0, 53)
            text("Ga Terug",55,75)
            #KNOP BEVESTIGING
            text("Vragen gereset naar originele staat!",250,205)
        
    def delete(self):
        if toevoeging == True:
            with open('questionsOriginal.json') as f:
                data = json.load(f)
    
            file_dupli = open("questions.json", "w")
            json.dump(data, file_dupli)
            file_dupli.close()
