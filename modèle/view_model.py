# File where we get into our database the entry of users
from .connection import Connection

class View_model():
    def __init__(self):
        self.db = Connection()
        self.author = ""
        self.content = ""
       
        
        

    #method for inserting message into the database
    def write_message(self):
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO message (content, publishing_date, author) VALUES (%s, NOW(), %s);", self.content, self.author)
        self.db.connection.commit()
        self.db.close_connection()
        


    def get_message(self):
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM message;")
        messages = self.db.cursor.fetchall()
        self.db.close_connection()
        print (messages)







