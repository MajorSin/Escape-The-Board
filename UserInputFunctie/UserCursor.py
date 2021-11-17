class UserCursor():
    def __init__(self, cursor_image):
        self.cursor_image = cursor_image
        
    def display(self):
        cursor_image = loadImage(self.cursor_image)
        image(cursor_image, mouseX, mouseY)
