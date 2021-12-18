class UserCursor():
    #Gereed stellen wat nodig is.
    def prep(self):
        #Laadt de afbeelding van de cursor in.
        global cursor_image
        cursor_image = loadImage("images/cursor.png")
        
    #Laadt alles in wat getoond moet worden.
    def display(self):
        # Zorgt dat de cursor uit de hoeken kan gaan 
        # en op tijd verschijnt.
        if not(mouseX == 0 or mouseY == 0):
            image(cursor_image, mouseX, mouseY)
