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
    size(1000, 1000)
    noStroke()
    noCursor()
    global background_image
    background_image = loadImage('images/horror-background.jpg')
    
def draw():
    global background_image
    background(background_image)
    textFont(createFont('Arial', 50))
    user_list.display()
    user_input.display()
    user_buttons.display()
    user_cursor.display()

def mousePressed():
    user_input.mousePressed()
    user_buttons.mousePressed()
    
def keyPressed():
    user_input.keyPressed()

        
    
