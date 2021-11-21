class UserButtons():
    edit = 100
    delete = 100
    reset = 100
    
    def __init__(self, user_list, user_input):
        self.user_list = user_list
        self.user_input = user_input
        
    def display(self):
        edit_image = loadImage('images/edit.png')
        delete_image = loadImage('images/delete.png')
        reset_image = loadImage('images/reset.png')
        
        editing = self.user_input.editing
        deleting = self.user_input.deleting

        if (editing and not(deleting)) or not(editing) and not(deleting):
            fill(self.edit)
            stroke(self.edit)
            rect(198, 800, 150, 100)
            image(edit_image, 245, 820)
      
        if (deleting and not(editing)) or not(deleting) and not(editing):  
            fill(self.delete)
            stroke(self.delete)
            rect(427, 800, 150, 100)
            image(delete_image, 469, 820)
        
        if not(deleting) and not(editing):
            fill(self.reset)
            stroke(self.reset)
            rect(650, 800, 150, 100)
            image(reset_image, 694, 820)
            
        UserButtons.check(self)
        
    def check(self):
        UserButtons.mouse_over(self)
        
    def mouse_over(self):
        edit_l = 198 <= mouseX <= 348
        delete_l = 428 <= mouseX <= 578
        reset_l = 650 <= mouseX <= 800
        
        if (edit_l or delete_l or reset_l) and 800 <= mouseY <= 900:
            if edit_l:
                self.edit = '#2d42ab'
            elif delete_l:
                self.delete = '#640700'
            else:
                self.reset = '#123900'
        else:
            self.edit = 100
            self.delete = 100 
            self.reset = 100
    
    def mousePressed(self):
        edit_l = 198 <= mouseX <= 348
        delete_l = 428 <= mouseX <= 578
        reset_l = 650 <= mouseX <= 800
        
        if (edit_l or delete_l or reset_l) and 800 <= mouseY <= 900:
            if edit_l:
                if self.user_list.users:
                    self.user_input.enable_editing()
            elif delete_l:
                if self.user_list.users:
                    self.user_input.enable_deleting()
            elif reset_l and not(self.user_input.deleting):
                self.user_list.reset_list()
