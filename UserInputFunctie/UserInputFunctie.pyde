from UserList import *
from UserInput import *
from UserButtons import *
from UserCursor import *
from User import *

user_list = UserList([])
user_input = UserInput('', False, 'images/error.png', 'images/error-2.png', 
'images/error-3.png', 'images/error-4.png', '#ffffff', False, user_list, 0, User, False)
user_buttons = UserButtons(100, 100, 100, user_list, user_input)
user_cursor = UserCursor('images/cursor.png')

background_image = loadImage('images/horror-background.jpg')

def setup():
    size(1000, 1000)
    noStroke()
    noCursor()
    global background_image
    background_image = loadImage('images/horror-background.jpg')
    
def draw():
    global background_image
    background(background_image)
    user_list.display()
    user_input.display()
    user_buttons.display()
    user_cursor.display()

def mousePressed():
    user_input.mousePressed()
    user_buttons.mousePressed()
    
def keyPressed():
    user_input.keyPressed()

        
    
