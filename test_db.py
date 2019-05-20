import sqlite3


connection = sqlite3.connect('C:\section5project/new.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'mark', 'asdf'),
    (3, 'joseph', 'asdf'),
    (4, 'tom', 'asdf')
]

cursor.executemany(insert_query, users)
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


connection.commit()

connection.close()