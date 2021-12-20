from Interface import *
from VraagInvoegen import *

#Alle objecten aanmaken die nodig zijn.
interface = InterFace()
vraag_invoegen = VraagInvoegen()

#Gereed stellen wat nodig is.
def prep():
    global current_screen
    current_screen = 'Interface'
    interface.prep()
    vraag_invoegen.prep()

#Laadt alles in wat getoond moet worden.
def data():
    #Toont wat nodig is op basis van het scherm. 
    if current_screen == 'Interface':
        interface.display()
    elif current_screen == 'QuestionInput':
        vraag_invoegen.display()
    
#Zorgt dat klikken wordt bijgehouden.
def mousePressed():
    interface.mousePressed()
