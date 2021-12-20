from UserCursor import *
import InterfaceMain, UserInputMain, CategoryMain
from VraagInvoegen import *
VraagInvoegen = VraagInvoegen()

user_cursor = UserCursor()

#Gereed stellen wat nodig is.
def prep():
    global current_screen
    current_screen = 'InterfaceMain'
    user_cursor.prep()
    InterfaceMain.prep()
    UserInputMain.prep()
    CategoryMain.prep()

#Laadt alles in wat getoond moet worden.
def display_screen():
    #Toont wat nodig is op basis van het scherm.   
    if current_screen == 'InterfaceMain':
        InterfaceMain.data()
    elif current_screen == 'UserInputMain':
        UserInputMain.data()
    elif current_screen == 'CategoryMain':
        CategoryMain.data()
    elif current_screen == 'CategoryMain':
        CategoryMain.data()
    elif current_screen == 'QuestionInput':
        VraagInvoegen.display()
        
    user_cursor.display()

def set_screen(screen):
    global current_screen
    
    if screen == 'InterfaceMain':
        current_screen = 'InterfaceMain'
    elif screen == 'UserInputMain':
        current_screen = 'UserInputMain'
    elif screen == 'CategoryMain':
        current_screen = 'CategoryMain'
    elif screen == 'QuestionInput':
        current_screen = 'QuestionInput'
    
#Zorgt dat klikken wordt bijgehouden.
def mousePressed():
    if current_screen == 'InterfaceMain':
        InterfaceMain.mousePressed()
    elif current_screen == 'UserInputMain':
        UserInputMain.mousePressed()
    elif current_screen == 'CategoryMain':
        CategoryMain.mousePressed()
    elif current_screen == 'QuestionInput':
        VraagInvoegen.mousePressed()
        

def keyPressed():
    if current_screen == 'UserInputMain':
        UserInputMain.keyPressed()