from UserList import *
from UserInput import *
from UserButtons import *
from UserCursor import *
from User import *

user_list = UserList([])
user_input = UserInput('', user_list, User)
user_buttons = UserButtons(user_list, user_input)
user_cursor = UserCursor('images/cursor.png')

background_image = ''

def setup():
    #Grootte van het spel.
    size(1000, 1000)
    
    #Stijl.
    noStroke()
    noCursor()
    
    #Achtergrond inladen.
    global background_image
    background_image = loadImage('images/horror-background.jpg')
    
def draw():
    #Dit ververst de achtergrond.
    global background_image
    background(background_image)
    
    #Standaard font tekst.
    textFont(createFont('Arial', 50))
    
    #Componenten van de functie tonen.
    user_list.display()
    user_input.display()
    user_buttons.display()
    user_cursor.display()

def mousePressed():
    #Zorgt dat klikken wordt bijgehouden.
    user_input.mousePressed()
    user_buttons.mousePressed()
    
def keyPressed():
    #Zorgt dat keyboard wordt bijgehouden.
    user_input.keyPressed()

        
    
