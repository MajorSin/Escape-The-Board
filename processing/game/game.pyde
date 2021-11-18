import json
from get import *

buttonPressedGetVragen = False
buttonPressedVraagInvoegen = False
errorScreenInput = False
buttonPressedResetten1 = False
buttonPressedResetten2 = False

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def setup():
    size(1080,900)
    background(0, 200, 0)

def draw():
    #AANVRAAG VRAGEN
    if buttonPressedGetVragen:
        background(0, 200, 0)
        fill(0, 102, 153)
        rect(25,25,200,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #JSON DATA
        import get
        #PRINT RESULT
        textSize(20)
        height = 150
        questions = 1
        for i in range(len(list)):
            main = list[i]
            if main['toevoeging'] == 'True':
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
    #BUTTON OM INVOEGEN
    elif buttonPressedVraagInvoegen:
        background(0, 200, 0)
        fill(0, 102, 153)
        rect(25,25,200,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #INVOEGEN
        text("Uw vraag was: " + vraag,400,175)
        text("Het antwoord is: " + antwoord,400,220)
        text("Bij de categorie: " + category,400,260)
        text("Uw vraag is toegevoegd!",400,300)
    #RESETTEN VRAGEN
    elif buttonPressedResetten1:
        background(0, 200, 0)
        fill(0, 102, 153)
        rect(25,25,200,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #BEVESTIGING
        fill(0, 102, 153)
        rect(300,205,450,100)
        fill(100, 0, 53)
        text("Weet u het zeker?",400,165)
        text("Ja",505,260)
    #ERROR SCREEN INPUT
    elif errorScreenInput:
        background(0, 200, 0)
        fill(0, 102, 153)
        rect(25,25,230,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #ERROR TEXT
        text("ERROR",400,175)
    else:
        #BASISSCHERM
        textSize(32)
        background(0, 200, 0)
        #ALLE VRAGEN OPHALEN
        fill(0, 102, 153)
        rect(300,100,450,100)
        fill(100, 0, 53)
        text("Laat alle vragen zien",400,155)
        #VRAGEN INZIEN
        fill(0, 102, 153)
        rect(300,250,450,100)
        fill(100, 0, 53)
        text("Vraag invoegen",400,305)
        #ALLES RESETTEN
        fill(0, 102, 153)
        rect(300,400,450,100)
        fill(100, 0, 53)
        text("Vragen resetten",400,455)
        text("Kies een optie:",400,50)
    #RESETTEN VRAGEN BEVESTIGING
    if buttonPressedResetten2:
        background(0, 200, 0)
        fill(0, 102, 153)
        rect(25,25,200,80)
        textSize(32)
        fill(100, 0, 53)
        text("Ga Terug",55,75)
        #KNOP BEVESTIGING
        text("Vragen gereset naar originele staat!",250,205)
        
def mousePressed():
    global buttonPressedGetVragen
    global buttonPressedVraagInvoegen
    global buttonPressedResetten1
    global buttonPressedResetten2
    global antwoord
    global vraag
    global category
    global errorScreenInput
    #BUTTON VOOR RUNNEN
    if 300 < mouseX < 300 + 450 and 100 < mouseY < 100 + 100 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == False:
        import get
        buttonPressedGetVragen = True
    #BUTTON VOOR INVOEGEN
    elif 300 < mouseX < 300 + 450 and 250 < mouseY < 250 + 100 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == False:
        #WELKE VRAAG TOEVOEGEN
        vraag = input('Welk vraag wilt u invoegen (kan niet leeg)?')
        #VRAAG LEGE INPUT
        if vraag == "" or vraag == " ":
            errorScreenInput = True
        #VRAAG VOLLEDIG
        elif vraag:
            #ANTWOORD INDIENEN
            antwoord = input('Wat is het antwoord (kan niet leeg)?')
            #ANTWOORD LEGE INPUT
            if antwoord == "" or antwoord == " ":
                errorScreenInput = True
            #ANTWOORD VOLLEDIG
            elif antwoord:
                #CATEGORIE INDIENEN
                category = input('In welk categorie? (kennis of wiskunde)?').lower()
                #CATEGORIE LEGE INPUT
                if category == "" or category == " ":
                    errorScreenInput = True
                #NIET GOED GEKOZEN
                elif category != 'kennis'and category != "wiskunde":
                    errorScreenInput = True
                #CATEGORIE VOLLEDIG
                elif category == 'kennis' or category == "wiskunde":
                    buttonPressedVraagInvoegen = True
                    entry = {"question": vraag, "answer": antwoord,"category": category, "toevoeging": 'True'}
                    filename = 'questions.json'
                    with open(filename, "r") as file:
                        data = json.load(file)
                    data.append(entry)
                    with open(filename, "w") as file:
                        json.dump(data,file)
                #ANNULERING = TERUGBRENGEN
                else:
                    buttonPressedVraagInvoegen = False
            #ANNULERING = TERUGBRENGEN
            else:
                buttonPressedVraagInvoegen = False
        #ANNULERING = TERUGBRENGEN
        else:
            buttonPressedVraagInvoegen = False
    #BUTTON VOOR RESETTEN VRAGEN
    elif 300 < mouseX < 300 + 450 and 400 < mouseY < 400 + 100 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == False:
        buttonPressedResetten1 = True
    #BUTTON VOOR BEVESTIGING RESETTEN VRAAG
    elif 300 < mouseX < 300 + 450 and 205 < mouseY < 205 + 100 and buttonPressedGetVragen == False and buttonPressedVraagInvoegen == False and buttonPressedResetten1 == True:
        buttonPressedResetten2 = True
        import reset
    #GA TERUG
    if 25 < mouseX < 25 + 200 and 25 < mouseY < 25 + 200:
        buttonPressedGetVragen = False
        buttonPressedVraagInvoegen = False
        errorScreenInput = False
        buttonPressedResetten1 = False
        buttonPressedResetten2 = False
