from model.view_model import View_model



class Message_view():
    def __init__(self):
        self.vm = View_model()
        

    def input_user(self):
        self.author = input("Enter your name")
        self.content = input ("Enter your message")

