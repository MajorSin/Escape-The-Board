#Importeert alle klassen die we nodig hebben.
from UserList import *
from UserInput import *
from UserButtons import *
from User import *

#Maakt alle objecten nodig van de klasses.
user_list = UserList([])
user_input = UserInput('', user_list, User)
user_buttons = UserButtons(user_list, user_input)

#Gereed stellen wat nodig is.
def prep():
    user_input.prep()
    user_buttons.prep()
    
#Laadt alles in wat getoond moet worden.
def data():
    #Componenten van de functie tonen.
    user_list.display()
    user_input.display()
    user_buttons.display()

#Zorgt dat klikken wordt bijgehouden.
def mousePressed():
    user_input.mousePressed()
    user_buttons.mousePressed()
    
#Zorgt dat keyboard wordt bijgehouden.
def keyPressed():
    user_input.keyPressed()
