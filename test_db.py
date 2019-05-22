import sqlite3
from models.database import DataBase


connection = sqlite3.connect(DataBase.db_path)
cursor = connection.cursor()
create_table = "CREATE TABLE IF NOT EXISTS registeredUsers (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
connection.commit()
connection.close()
