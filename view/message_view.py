from modèle.view_model import View_model

class MessageView:
    def __init__(self):
        self.vm = View_model()
    
    def input_message(self):
        self.author = input("Enter your name: ")
        self.content = input("Enter your message: ")
        self.vm.write_message()
    
    def display_message(self):
        self.vm.get_message()