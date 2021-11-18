class UserInput():
    def __init__(self, input, pressed_enter, error, error_2, hovering, clicked, user_list, user_id):
        self.input = input
        self.pressed_enter = pressed_enter
        self.error = error
        self.error_2 = error_2
        self.hovering = hovering
        self.clicked = clicked
        self.user_list = user_list
        self.user_id = user_id
        
    def display(self):
        input = self.input
        pressed_enter = self.pressed_enter
        error = loadImage(self.error)
        error_2 = loadImage(self.error_2)
        hovering = self.hovering
        clicked = self.clicked
        user_list = self.user_list
        
        fill(40)
        stroke(hovering)
        strokeWeight(5)
        rect(200, 250, 600, 100)
        
        textFont(createFont('Arial', 50))
        textSize(70)
        
        if input:
            fill(255)
            text(input, 220, 325)
        elif (not(input) and pressed_enter) and not(len(user_list.users) == 4):
            error.resize(500, 80)
            image(error, 250, 100) 
        elif clicked == False:
            fill(hovering)
            textSize(45)
            text('Klik om speler toe te voegen', 218, 318)
        
        if len(user_list.users) == 4 and pressed_enter:
            error_2.resize(500, 80)
            image(error_2, 250, 100)
        
        UserInput.check(self)
    
    def check(self):
        UserInput.mouse_hover(self)
        
    def keyPressed(self):
        input = self.input
        pressed_enter = self.pressed_enter
        clicked = self.clicked
        user_list = self.user_list
        error = loadImage(self.error)
        user_id = self.user_id
        
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
                if len(user_list.users) < 4:
                    user_id += 1
                    self.user_id = user_id
                    user = {'id': user_id, 'name': input, 'score': 0}
                    user_list.add_user(user)
                    pressed_enter = False
                input = ''
                clicked = False
                
            self.input = input
            self.pressed_enter = pressed_enter
            self.clicked = clicked
            
    def mouse_hover(self):
        if (200 <= mouseX <= 800) and (250 <= mouseY <= 350):
            self.hovering = '#00f1fe'
        else:
            self.hovering = '#ffffff'
            
    def mousePressed(self):
        if (mouseX >= 200 and mouseX <= 800) and (mouseY >= 250 and mouseY <= 350):
            self.clicked = True
        else:
            self.clicked = False
            
