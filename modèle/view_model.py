# File where we get into our database the entry of users
from .connection import Connection

class View_model():
    def __init__(self):
        self.db = Connection()
        
       
        
        

    #method for inserting message into the database
    def write_message(self, content, author):
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO message (content, publishing_date, author) VALUES (%s, NOW(), %s);", (content, author))
        self.db.connection.commit()
        self.db.close_connection()
        


    def get_message(self):
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM message;")
        messages = self.db.cursor.fetchall()
        self.db.close_connection()
        return messages







