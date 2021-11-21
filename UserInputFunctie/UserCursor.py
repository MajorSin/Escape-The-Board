class UserCursor():
    def __init__(self, cursor_image):
        self.cursor_image = cursor_image
        
    def display(self):
        cursor_image = loadImage(self.cursor_image)
        if not(mouseX == 0 or mouseY == 0):
            image(cursor_image, mouseX, mouseY)
