from CategoryButtons import *
from Category import *
from UserCursor import *

#Alle objecten aanmaken die nodig zijn.
user_cursor = UserCursor()
category_buttons = CategoryButtons()
category = Category()

#Gereed stellen wat nodig is.
def prep():
    global current_screen
    current_screen = 'Categories'
    user_cursor.prep()
    category_buttons.prep()
    category.prep()

#Laadt alles in wat getoond moet worden.
def display_screen():
    #Toont wat nodig is op basis van het scherm.   
    if current_screen == 'Categories':
        category_buttons.display()
    elif current_screen == 'Category':
        category.display()
        
    user_cursor.display()

def set_screen(chosen_category):
    global current_screen
    
    if current_screen == 'Categories':
        current_screen = 'Category'
        if chosen_category == 'Standard':
            category.set_category('Standard')
        elif chosen_category == 'Knowledge':
            category.set_category('Knowledge')
        else:
            category.set_category('Math')
    else:
        current_screen = 'Categories'
        category.set_category('')
    
#Zorgt dat klikken wordt bijgehouden.
def mousePressed():
    category_buttons.mousePressed()
    category.mousePressed()
