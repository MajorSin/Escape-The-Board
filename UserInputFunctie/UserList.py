class UserList():
    def __init__(self, users):
        self.users = users
        
    def display(self):
        fill(255)
        stroke(255)
        textSize(50)
        text('Spelers:', 192, 450)
        line(198, 480, 798, 480);
        
        if self.users:
            textSize(40)
            temp = 550
            for user in self.users:
                text('Speler ' + str(user.id) + ': ' + str(user.name), 192, temp)
                temp += 50
         
    def add_user(self, user):
        user = user
        self.users.append(user)
    
    def edit_user(self, user_id, name):
        user = user_id
        
        for index in self.users:
            if index.id == user:
                index.name = name 
                
    def delete_user(self, user_id):
        user = user_id
        
        for index in self.users:
            if index.id == user:
                self.users.remove(index)
                
        temp = 1
        for user in self.users:
            user.id = temp
            temp += 1
        
    def reset_list(self):
        self.users = []
    
                
