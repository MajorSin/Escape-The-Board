#IMPORT FILES
from moeilijk import *
from makkelijk import *

#IMPORT CLAS
moeilijk = moeilijk()
makkelijk = makkelijk()

#STANDARD VARIABLES
moeilijkButton = False
makkelijkButton = False

def setup():
    size(1080,900)
    background(0, 200, 0)
    
def draw():
    #MOEILIJKE KNOP
    if moeilijkButton:
        pass
    #MAKKELIJK KNOP
    elif makkelijkButton:
        pass
    #BASISSCHERM
    else:
        background(0, 200, 0)
        textSize(32)
        fill(100, 0, 53)
        text("Kies een optie:", 400, 50)
        #MOEILIJK KNOP
        fill(0, 102, 153)
        rect(300,100,450,100)
        fill(100, 0, 53)
        text("Moeilijke vraag",400,155)
        #MAKKELIJK KNOP
        fill(0, 102, 153)
        rect(300,250,450,100)
        fill(100, 0, 53)
        text("Makkelijke vraag",400,305)
    
def mousePressed():
    global moeilijkButton
    global makkelijkButton
    #MOEILIJKE VRAAG BUTTONS
    if 300 < mouseX < 300 + 450 and 100 < mouseY < 100 + 100 and moeilijkButton == False and makkelijkButton == False:
        moeilijkButton = True
        moeilijk.display(moeilijkButton)
    #MAKKELIJKE VRAAG BUTTONS
    elif 300 < mouseX < 300 + 450 and 250 < mouseY < 250 + 100 and moeilijkButton == False and makkelijkButton == False:
        makkelijkButton = True
        makkelijk.display(makkelijk)
    #ANTWOORD MOEILIJKE VRAAG
    elif 300 < mouseX < 300 + 475 and 210 < mouseY < 210 + 100 and moeilijkButton == True and makkelijkButton == False:
        moeilijk.antwoord()
    #ANTWOORD MAKKELIJKE VRAAG
    elif 300 < mouseX < 300 + 475 and 210 < mouseY < 210 + 100 and moeilijkButton == False and makkelijkButton == True:
        makkelijk.antwoord()
        print("Antwoord makkelijke vraag BASIS SCHERM")
    #GA TERUG
    if 25 < mouseX < 25 + 200 and 25 < mouseY < 25 + 200:
        moeilijkButton = False
        makkelijkButton = False
        
