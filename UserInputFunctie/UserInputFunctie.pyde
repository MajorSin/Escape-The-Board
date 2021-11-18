from UserInput import *
from UserCursor import *
from UserList import *

user_list = UserList([])
user_input = UserInput('', False, 'images/error.png', 'images/error-2.png', '#ffffff', False, user_list, 0)
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
    user_input.display()
    user_list.display()
    user_cursor.display()

def mousePressed():
    user_input.mousePressed()
    
def keyPressed():
    user_input.keyPressed()

        
    
