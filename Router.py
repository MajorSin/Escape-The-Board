from CategoryButtons import *
from Category import *
from CategoryQuestion import *
from UserCursor import *
from obstakelScreen import *

#Alle objecten aanmaken die nodig zijn.
user_cursor = UserCursor()
category_buttons = CategoryButtons()
category_question = CategoryQuestion()
obstakel = obstakel()
category = Category(category_question, obstakel)

#Gereed stellen wat nodig is.
def prep():
    global current_screen
    current_screen = 'Categories'
    user_cursor.prep()
    category_buttons.prep()
    category.prep()
    category_question.prep()

#Laadt alles in wat getoond moet worden.
def display_screen():
    #Toont wat nodig is op basis van het scherm.   
    if current_screen == 'Categories':
        category_buttons.display()
    elif current_screen == 'Category':
        category.display()
    elif current_screen == 'Question':
        category_question.display()
    elif current_screen == 'Obstakel':
        obstakel.display()
        
    user_cursor.display()

def set_screen(screen):
    global current_screen
    
    if screen == 'Categories':
        current_screen = 'Categories'
    elif screen == 'Standard':
        current_screen = 'Category'
        category.set_category('Standard')
    elif screen == 'Knowledge':
        current_screen = 'Category'
        category.set_category('Knowledge')
    elif screen == 'Math':
        current_screen = 'Category'
        category.set_category('Math')
    elif screen == 'Category':
        current_screen = 'Category'
    elif screen == 'Question':
        current_screen = 'Question'
    elif screen == 'Obstakel':
        current_screen = 'Obstakel'
    else:
        current_screen == 'Categories'
    
#Zorgt dat klikken wordt bijgehouden.
def mousePressed():
    if current_screen == 'Categories':
        category_buttons.mousePressed()
    elif current_screen == 'Category':
        category.mousePressed()
    elif current_screen == 'Obstakel':
        obstakel.mousePressed()
    else:
        category_question.mousePressed()
    
    
