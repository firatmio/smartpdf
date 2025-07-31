import os

class Session:
    def __init__(self):
        self.app_folder = os.path.join(os.path.expanduser("~"), ".smartpdf")
    
    def check(self):
        if not os.path.exists(self.app_folder):
            #self.create_session()
            return False
        return True
    
    def create_session(self):
        os.makedirs(self.app_folder)
            
    def __str__(self):
        return str(self.check())