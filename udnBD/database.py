from sqlite3 import Cursor
import string
import pymongo
from dotenv import load_dotenv
import os
#Clase para crear conexión a la base de datos de MongoDB.

class Database:

    def __init__(self, table: string) -> "Database":
        load_dotenv()
        self.client = pymongo.MongoClient(f"mongodb+srv://{os.getenv('dbuser')}:{os.getenv('password')}@udeninos.lyt70.mongodb.net/?retryWrites=true&w=majority")
        self.dbname = self.client["BD_UDENINOS"]
        self.collection = self.dbname[table] 
    
    def see_all(self):
        return self.collection.find({})

    def see_filtered(self, key, value):
        return self.collection.find({key:value})

    def print_query(self, cursor: Cursor):
        for match in cursor:
            print(match)

if __name__ == "__main__":

    test = Database("BD_profesores")
    profes = test.see_all()
    oscar = test.see_filtered("Nombres y apellidos", "OSCAR GALLO")
    test.print_query(oscar)