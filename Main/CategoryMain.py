from CategoryButtons import *
from Category import *
from CategoryQuestion import *
from Leaderboard import *
from obstakelScreen import *

#Alle objecten aanmaken die nodig zijn.
leaderboard = Leaderboard([], 1)
category_buttons = CategoryButtons()
category_question = CategoryQuestion(leaderboard)
category = Category(category_question, obstakel())

#Gereed stellen wat nodig is.
def prep():
    global current_screen
    current_screen = 'Categories'
    category_buttons.prep()
    category.prep()
    category_question.prep()
    leaderboard.prep()

#Laadt alles in wat getoond moet worden.
def data():
    #Toont wat nodig is op basis van het scherm.   
    if current_screen == 'Categories':
        category_buttons.display()
    elif current_screen == 'Category':
        category.display()
        leaderboard.display()
    elif current_screen == 'Question':
        category_question.display()
    
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
    else:
        current_screen == 'Categories'
        
def set_leaderboard(user_list):
    category.chosen_category = ''
    leaderboard.user_list = user_list
    leaderboard.current_user = 1
    
#Zorgt dat klikken wordt bijgehouden.
def mousePressed():
    if current_screen == 'Categories':
        category_buttons.mousePressed()
    elif current_screen == 'Category':
        category.mousePressed()
    else:
        category_question.mousePressed()
