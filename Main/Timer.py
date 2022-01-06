class Timer():
    time = 0
    
    def __init__(self, time):
        self.time = time
    
    def set_time(self, time):
        self.time = time
        
    def get_time(self):
        return int(self.time)
        
    def count_down(self):
        self.time -= 1/frameRate
