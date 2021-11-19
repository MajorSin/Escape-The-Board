class UserButtons():
    def __init__(self, edit, delete, reset, user_list, user_input):
        self.edit = edit
        self.delete = delete
        self.reset = reset
        self.user_list = user_list
        self.user_input = user_input
        
    def display(self):
        edit_image = loadImage('images/edit.png')
        delete_image = loadImage('images/delete.png')
        reset_image = loadImage('images/reset.png')
        
        edit = self.edit
        delete = self.delete
        reset = self.reset
        user_list = self.user_list
        
        fill(edit)
        stroke(edit)
        rect(198, 800, 150, 100)
        
        fill(delete)
        stroke(delete)
        rect(426, 800, 150, 100)
        
        fill(reset)
        stroke(reset)
        rect(650, 800, 150, 100)
        
        image(edit_image, 245, 820)
        image(delete_image, 468, 820)
        image(reset_image, 694, 820)
            
        UserButtons.check(self)
        
    def check(self):
        UserButtons.mouse_over(self)
        
    def mouse_over(self):
        edit = self.edit
        delete = self.delete
        reset = self.reset
        
        edit_l = 198 <= mouseX <= 348
        delete_l = 428 <= mouseX <= 578
        reset_l = 650 <= mouseX <= 800
        
        if (edit_l or delete_l or reset_l) and 800 <= mouseY <= 900:
            if edit_l:
                edit = '#2d42ab'
            elif delete_l:
                delete = '#640700'
            else:
                reset = '#123900'
        else:
            edit = 100
            delete = 100 
            reset = 100
            
        self.edit = edit
        self.delete = delete
        self.reset = reset
    
    def mousePressed(self):
        edit_l = 198 <= mouseX <= 348
        delete_l = 428 <= mouseX <= 578
        reset_l = 650 <= mouseX <= 800
        user_list = self.user_list
        user_input = self.user_input
        
        if (edit_l or delete_l or reset_l) and 800 <= mouseY <= 900:
            if edit_l:
                print('In behandeling')
            elif delete_l:
                if user_list.users:
                    user_input.enable_deleting()
            else:
                user_list.reset_list()
    
