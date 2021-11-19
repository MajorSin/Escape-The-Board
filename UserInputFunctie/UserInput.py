class UserInput():
    def __init__(self, input, pressed_enter, error, 
        error_2, error_3, error_4, hovering, clicked, 
        user_list, user_id, user, deleting):
        self.input = input
        self.pressed_enter = pressed_enter
        self.error = error
        self.error_2 = error_2
        self.error_3 = error_3
        self.error_4 = error_4
        self.hovering = hovering
        self.clicked = clicked
        self.user_list = user_list
        self.user_id = user_id
        self.user = user
        self.deleting = deleting
        
    def display(self):
        input = self.input
        pressed_enter = self.pressed_enter
        error = loadImage(self.error)
        error_2 = loadImage(self.error_2)
        error_3 = loadImage(self.error_3)
        error_4 = loadImage(self.error_4)
        hovering = self.hovering
        clicked = self.clicked
        user_list = self.user_list
        deleting = self.deleting
        
        fill(40)
        stroke(hovering)
        strokeWeight(5)
        textFont(createFont('Arial', 50))
        textSize(70)
        
        if not(deleting):
            rect(200, 250, 600, 100)
            if input:
                fill(255)
                text(input, 220, 325)
            elif not(input) and pressed_enter:
                error.resize(500, 80)
                image(error, 250, 100) 
            elif clicked == False:
                fill(hovering)
                textSize(45)
                text('Klik om speler toe te voegen', 218, 318)
            
            characters = len(input) < 3 or len(input) > 16
            
            if len(user_list.users) == 4 and pressed_enter and not(characters):
                error_2.resize(500, 80)
                image(error_2, 250, 100)
            elif (characters) and (pressed_enter and input):
                if len(input) < 3:
                    error_3.resize(500, 80)
                    image(error_3, 250, 100)
                else:
                    error_4.resize(500, 80)
                    image(error_4, 250, 100)
                            
            UserInput.check(self)
        else:
            fill(255)
            textSize(50)
            text('Druk het spelernummer in \nom de speler te verwijderen!', 198, 250)
    
    def check(self):
        UserInput.check_users(self)
        UserInput.mouse_hover(self)
        
    def enable_deleting(self):
        deleting = self.deleting
        deleting = True
        self.deleting = deleting
        
    def keyPressed(self):
        input = self.input
        pressed_enter = self.pressed_enter
        clicked = self.clicked
        user_list = self.user_list
        user_id = self.user_id
        user = self.user
        deleting = self.deleting
        
        if clicked == True:
            if ('A' <= key >= 'Z') and not(key == ' '):
                pressed_enter = False
                if not(input):
                    input += key.capitalize()
                else:
                    input += key
            elif key == BACKSPACE:
                input = input[:-1]
            elif key == ENTER and not(input):
                pressed_enter = True
            elif key == ENTER and input:
                pressed_enter = True
                if len(user_list.users) < 4 and not(len(input) < 3 or len(input) > 16):
                    if len(user_list.users) == 0:
                        user_id = 0
                    user_id = user_id + 1    
                    user = user(user_id, input, 0)
                    user_list.add_user(user)
                    pressed_enter = False
                    self.user_id = user_id
                    input = ''
                    clicked = False
                
            self.input = input
            self.pressed_enter = pressed_enter
            self.clicked = clicked
            
        if deleting:
            if '1' <= key <= '4':
                user_list.delete_user(key)
                self.deleting = False
            
    def check_users(self):
        user_list = self.user_list
        user_id = self.user_id
        
        if not(len(user_list.users) == user_id):
            user_id = len(user_list.users)
            self.user_id = user_id
        
    def mouse_hover(self):
        if (200 <= mouseX <= 800) and (250 <= mouseY <= 350):
            self.hovering = '#00f1fe'
        else:
            self.hovering = '#ffffff'
            
    def mousePressed(self):
        if (200 <= mouseX <= 800) and (250 <= mouseY <= 350):
            self.clicked = True
        else:
            self.clicked = False
            
