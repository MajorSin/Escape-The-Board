class UserCursor():
    def __init__(self, cursor_image):
        self.cursor_image = cursor_image
    
    #Laadt alles in wat getoond moet worden.
    def display(self):
        #Laadt de afbeelding van de cursor in.
        cursor_image = loadImage(self.cursor_image)
        
        # Zorgt dat de cursor uit de hoeken kan gaan 
        # en op tijd verschijnt.
        if not(mouseX == 0 or mouseY == 0):
            image(cursor_image, mouseX, mouseY)
