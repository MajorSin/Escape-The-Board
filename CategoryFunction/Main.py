#Importeert alle klassen die we nodig hebben.
from CategoryButtons import *
from UserCursor import *

#Maakt alle objecten nodig van de klasses.
category_buttons = CategoryButtons()
user_cursor = UserCursor()

#Gereed stellen wat nodig is.
def prep():
    category_buttons.prep()
    user_cursor.prep()
    
#Laadt alles in wat getoond moet worden.
def data():
    #Componenten van de functie tonen.
    category_buttons.display()
    user_cursor.display()

#Zorgt dat klikken wordt bijgehouden.
# def mousePressed():
#     user_input.mousePressed()
#     user_buttons.mousePressed()
    
#Zorgt dat keyboard wordt bijgehouden.
# def keyPressed():
#     user_input.keyPressed()
