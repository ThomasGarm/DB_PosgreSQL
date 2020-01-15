from modèle.view_model import View_model

class MessageView:
    def __init__(self):
        self.vm = View_model()
        
    
    def input_message(self):
        author = input("Enter your name: ")
        content = input("Enter your message: ").upper()
        self.vm.write_message(content, author)
    
    def display_message(self):
        view = self.vm.get_message()
        for element in view:
            print(f"Message from: {element[3]}, Date:{element[2]}\n [{element[1]}]")
            print("=============================================================")